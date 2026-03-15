import json
import time
import uuid
import logging
import redis

logger = logging.getLogger(__name__)


class QueueManager:
    """
    Distributed queue manager using Redis.
    Supports atomic job claiming, retries, and dead-letter queues.
    """

    def __init__(
        self,
        host="localhost",
        port=6379,
        password=None,
        db=0,
        job_queue="scraper:jobs:pending",
        working_queue="scraper:jobs:working",
        dlq="scraper:jobs:dlq",
        max_retries=3,
        timeout_seconds=300,
    ):
        self.redis = redis.Redis(
            host=host, port=port, password=password, db=db, decode_responses=True
        )
        self.job_queue = job_queue
        self.working_queue = working_queue
        self.dlq = dlq
        self.max_retries = max_retries
        self.timeout_seconds = timeout_seconds

    def enqueue(self, url, metadata=None):
        """Push a new URL to the pending queue."""
        job = {
            "id": str(uuid.uuid4()),
            "url": url,
            "metadata": metadata or {},
            "retries": 0,
            "status": "pending",
            "created_at": time.time(),
        }
        self.redis.lpush(self.job_queue, json.dumps(job))
        logger.info(f"Enqueued job {job['id']} for {url}")
        return job["id"]

    def fetch_job(self):
        """
        Atomically move a job from the pending queue to the working queue.
        Returns the job dictionary or None.
        """
        # RPOPLPUSH is atomic. For Redis >= 6.2, BRPOPLPUSH is replaced by BLMOVE/LMOVE.
        # We use RPOPLPUSH for simplicity and backward compatibility.
        raw_job = self.redis.rpoplpush(self.job_queue, self.working_queue)
        if not raw_job:
            return None

        job = json.loads(raw_job)  # type: ignore
        job["started_at"] = time.time()

        # Update the job in the working queue (remove old, push new)
        self.redis.lrem(self.working_queue, 1, raw_job)  # type: ignore
        self.redis.lpush(self.working_queue, json.dumps(job))

        return job

    def complete_job(self, job):
        """Acknowledge job completion and remove from working queue."""
        raw_job = json.dumps(job)
        # In a real scenario we'd match the ID rather than the exact raw string,
        # but for this example we assume the worker holds the exact state object.
        # Let's find it by ID just to be safe.

        # Type ignored because the redis type stubs sometimes incorrectly infer Awaitable for sync clients
        jobs: list[str] = self.redis.lrange(self.working_queue, 0, -1)  # type: ignore
        for j in jobs:
            parsed = json.loads(j)
            if parsed["id"] == job["id"]:
                self.redis.lrem(self.working_queue, 1, j)
                logger.info(f"Job {job['id']} completed successfully.")
                # Could optionally push to a "scraper:jobs:completed" queue
                return True

        logger.warning(f"Could not find job {job['id']} in working queue to complete.")
        return False

    def fail_job(self, job, error_message):
        """Mark job as failed. Retry if under limit, else push to DLQ."""
        # Type ignored because the redis type stubs sometimes incorrectly infer Awaitable for sync clients
        jobs: list[str] = self.redis.lrange(self.working_queue, 0, -1)  # type: ignore
        found_job = None
        for j in jobs:
            parsed = json.loads(j)
            if parsed["id"] == job["id"]:
                found_job = j
                self.redis.lrem(self.working_queue, 1, j)
                break

        if not found_job:
            logger.warning(f"Failed job {job['id']} not in working queue.")
            return

        job["retries"] += 1
        job["error"] = error_message

        if job["retries"] <= self.max_retries:
            logger.info(
                f"Retrying job {job['id']} (attempt {job['retries']}/{self.max_retries})"
            )
            # Push back to the pending queue
            self.redis.lpush(self.job_queue, json.dumps(job))
        else:
            logger.error(f"Job {job['id']} exceeded retries. Moving to DLQ.")
            job["failed_at"] = time.time()
            self.redis.lpush(self.dlq, json.dumps(job))

    def recover_stuck_jobs(self):
        """Identify jobs in working queue that exceeded timeout and requeue them."""
        # This should be run via a periodic cron or background thread on a orchestrator.
        pass
