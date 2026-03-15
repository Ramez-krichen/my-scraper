import logging
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any
from queue_manager import QueueManager
from pathlib import Path
import yaml

# Loading Config
def load_config(path=Path.cwd() / "config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

config = load_config()
redis_cfg = config["redis"]

# Initializing QueueManager
qm = QueueManager(
    host=redis_cfg["host"],
    port=redis_cfg["port"],
    password=redis_cfg["password"],
    db=redis_cfg["db"],
    job_queue=redis_cfg["job_queue"],
    working_queue=redis_cfg["working_queue"],
    dlq=redis_cfg["dead_letter_queue"],
    max_retries=redis_cfg["max_retries"],
    timeout_seconds=redis_cfg["timeout_seconds"],
)

# Setup FastAPI
app = FastAPI(title="Stealth Scraper API", description="API to submit scraper jobs and get webhooks.")

class JobRequest(BaseModel):
    url: HttpUrl
    metadata: Optional[Dict[str, Any]] = None

@app.post("/jobs", status_code=202)
def create_job(request: JobRequest):
    """
    Submit a scraping job to the Redis queue.
    If 'webhook_url' is provided in the metadata, a webhook will be sent to the 
    specified URL when the scrape successfully completes.
    """
    try:
        metadata = request.metadata or {}
        
        # enqueue job into Redis
        job_id = qm.enqueue(str(request.url), metadata=metadata)
        
        return {
            "status": "processing",
            "message": "Job enqueued successfully",
            "job_id": job_id
        }
    except Exception as e:
        logging.error(f"Failed to enqueue job: {e}")
        raise HTTPException(status_code=500, detail="Internal server error while enqueueing job")

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
