from product_detection import ProductListExtractor

def sotic_tn_products_page():
    return """
    
<!DOCTYPE html>
<html lang="en">
<head>

	    <base href="https://www.sotic.tn/"> 
  	
  		<!-- Required meta tags -->    
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" sizes="16x16" href="media/site/favicon-favicon.webp">    
        
    <title>Produits béton</title>
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="ONLYTECH">
        <meta property="og:title" content="Produits béton" />
    <meta property="og:description" content="" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://www.sotic.tn/" />
    <meta property="og:image" content="https://www.sotic.tn/media/site/logo-logo.webp" />
     
      	
  	<!-- Custom Font awesome -->
      	<!-- Custom Font awesome -->
        <link rel="stylesheet" href="dist/fontawesome-free-6.5.1-web/css/all.min.css">
        
        <link rel="stylesheet" href="dist/fonts/icomoon/style.css">
    
  	<!-- Latest compiled and minified CSS -->
	
	<link rel="preconnect" href="https://fonts.gstatic.com">

	<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
	
	<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">


	<!--- Animation ------------------------>	

	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.css" />

	<link href="https://www.jqueryscript.net/css/jquerysctipttop.css" rel="stylesheet" type="text/css">
	
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.5.0/css/flag-icon.min.css" type="text/css">


	<!--- Style ------------------------>	

	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <link rel="stylesheet" href="dist/css/style.css" />
	
	<link rel="stylesheet" href="dist/css/jquery-ui.min.css" />

    <link href="assets/vendor/aos/aos.css" rel="stylesheet">
    
    <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
    
    <!-- Include jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

	<!-- Bootstap Scripts -->
  
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/rateYo/2.3.2/jquery.rateyo.min.css">
	
    
	
  

    <script language = "Javascript" type="text/javascript">

    function echeck(str) {

		var at="@";

		var dot=".";

		var lat=str.indexOf(at);

		var lstr=str.length;

		var ldot=str.indexOf(dot);

		if (str.indexOf(at)==-1){

		   alert("Adresse email invalide.");
		   return false;

		}

		else if (str.indexOf(at)==-1 || str.indexOf(at)==0 || str.indexOf(at)==lstr){

		   alert("Adresse email invalide.");
		   return false;

		}

		else if (str.indexOf(dot)==-1 || str.indexOf(dot)==0 || str.indexOf(dot)==lstr){

		    alert("Adresse email invalide.");
		    return false;

		}

		else if (str.indexOf(at,(lat+1))!=-1){

		    alert("Adresse email invalide.");
		    return false;

		 }

		 else if (str.substring(lat-1,lat)==dot || str.substring(lat+1,lat+2)==dot){

		    alert("Adresse email invalide.");
		    return false;

		 }

		 else if (str.indexOf(dot,(lat+2))==-1){

		    alert("Adresse email invalide.");
		    return false;
		 }

		 else if (str.indexOf(" ")!=-1){

		    alert("Adresse email invalide.");
		    return false;
		 }

		 else {return true;}		 					

	}

</script>

    <script type="text/javascript" language="javascript">

	var request = makeObject1();

	function makeObject1()

	{

		var x;

		var browser = navigator.appName;

		if(browser == "Microsoft Internet Explorer")

		{

			x = new ActiveXObject("Microsoft.XMLHTTP");

		}

		else

		{

			x = new XMLHttpRequest();

		}

		return x;

	}

	function get_value1()

	{

		if(document.newsletter.mail.value=="")

		{

			alert("Entrez une adresse email ");

			return false;

			

		}

		else if (echeck(document.newsletter.mail.value)==false){

		return false;

    	}

		else

		{

			email = document.newsletter.mail.value;

			url = "abonnez-vous.php";

			url = url +'?email='+ email;

			//alert(url);	
			request.open('get', url);

			request.onreadystatechange = parseInfo1;

			request.send('');

			return false;

		}

	}

	function get_value()

	{

		if(document.newsletter1.mail.value=="")

		{

			alert("Entrez une adresse email ");

			return false;

			

		}

		else if (echeck(document.newsletter1.mail.value)==false){

		return false;

    	}

		else

		{

			email = document.newsletter1.mail.value;

			url = "abonnez-vous.php";

			url = url +'?email='+ email;

			//alert(url);	

			request.open('get', url);

			request.onreadystatechange = parseInfo;

			request.send('');

			return false;

		}

	}

	function parseInfo1()

	{

		if(request.readyState == 1)
		{
		return false;	
		}
		if(request.readyState == 4)
		{
			var answer = request.responseText;
			document.newsletter.mail.value=answer;
			//alert(answer);
		}
	}

	function parseInfo()

	{

		if(request.readyState == 1)
		{
		return false;	
		}
		if(request.readyState == 4)
		{
			var answer = request.responseText;
			document.newsletter1.mail.value=answer;
			//alert(answer);
		}
	}
	
	function parseInfo2()

	{

		if(request.readyState == 1)
		{
		return false;	
		}
		if(request.readyState == 4)
		{
			var answer = request.responseText;
			document.newsletter2.mail.value=answer;
			//alert(answer);
		}
	}
	
</script>	
	<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MFGP3PBZ');</script>
<!-- End Google Tag Manager -->
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1231130695193128');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1231130695193128&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->	
			
        <script language = "Javascript" type="text/javascript">

    function refreshPage() {
        location.reload(true);
    }

	function addToCart(product_id, quantity) {
		$.ajax({
			url: 'cart.php',
			type: 'GET',
			data: 'id_produit=' + product_id + '&quantity=' + quantity + '&action=add',
		    dataType: "json",
			success: function(data) {
			  $("#myAlert").fadeIn(1000);		
				setTimeout(function() { 
				   $("#myAlert").fadeOut(1000);							   
				}, 5000);
				
        		document.getElementById('compteurArticle').innerHTML= data['0'];
        		document.getElementById('blocDepartementsPanier').innerHTML= data['1'];
				
    		   $('html, body').animate({ scrollTop: 0 }, 'slow');
              
			},
			error: function (data) {
				console.log('Error:', data);
			}
		}); 
	}

    
    
    function modifierQteCart(product_id, quantity,option) {
    	 var quantity = parseInt(quantity);
    	$.ajax({ 
    		url: 'cart.php',
    		type: 'GET',
    		data: 'id_produit=' + product_id + '&quantity=' + quantity+ '&option=' + option +  '&action=mod',
    		dataType: "json",
    		success: function(data) { 	
				document.getElementById('compteurArticle').innerHTML= data['0']; 
				document.getElementById('blocDepartementsPanier').innerHTML= data['1'];
				document.getElementById('prixCommande').innerHTML= data['3'];
    		},
    		error: function (data) {
                console.log('Error:', data);
            }
    	});
    }
	function UpdatePlusProductCart(product_id, quantity,option) {
	    if(option != 0){
    	var qty   = parseInt(document.getElementById('qtybutton_'+option).value);
    	var prix   = document.getElementById('unit_price_'+option).value;
    	var quantity = parseInt(qty+1);
         document.getElementById('qtybutton_'+option).value= quantity;
    	 document.getElementById('total_ligne_panier_'+option).innerHTML= ((prix*quantity).toFixed(2)) + " DT";
	    }else{
    	var qty   = parseInt(document.getElementById('qtybutton_'+ product_id).value);
    	var prix   = document.getElementById('unit_price_'+ product_id).value;
    	var quantity = parseInt(qty+1);
         document.getElementById('qtybutton_'+product_id).value= quantity;
    	 document.getElementById('total_ligne_panier_'+product_id).innerHTML= ((prix*quantity).toFixed(2)) + " DT";
	    }
    	 modifierQteCart(product_id, quantity,option);
	}
	function UpdateMoinProductCart(product_id, quantity,option) {
	    if(option != 0){
    	var qty   = parseInt(document.getElementById('qtybutton_'+option).value);
    	var prix   = document.getElementById('unit_price_'+option).value;
    	var quantity = parseInt(qty-1);
        	if(quantity > 0){
             document.getElementById('qtybutton_'+option).value= quantity;
        	 document.getElementById('total_ligne_panier_'+option).innerHTML= ((prix*quantity).toFixed(2)) + " DT";
        	}
	    }else{
    	var qty   = parseInt(document.getElementById('qtybutton_'+ product_id).value);
    	var prix   = document.getElementById('unit_price_'+ product_id).value;
    	var quantity = parseInt(qty-1);
        	if(quantity > 0){
             document.getElementById('qtybutton_'+product_id).value= quantity;
        	 document.getElementById('total_ligne_panier_'+product_id).innerHTML= ((prix*quantity).toFixed(2)) + " DT";
        	}
	    }
        
		modifierQteCart(product_id, quantity,option);
	}
	/*function RemoveProductCart(product_id,option) {
		$.ajax({
			url: 'cart.php',
			type: 'GET',
			data: 'id_produit=' + product_id + '&option=' + option + '&action=remove',
			success: function(data) { 	
			  document.getElementById("blocDepartementsPanier").innerHTML = data[0];
			  document.getElementById("shopping__cart").innerHTML = data[1];
			  $('html, body').animate({ scrollTop: 0 }, 'slow');
			}
		});
	}*/
	function RemoveProductPanier(product_id,option) {
		$.ajax({
			url: 'cart.php',
			type: 'GET',
			data: 'id_produit=' + product_id + '&option=' + option + '&action=remove',
		    dataType: "json",
			success: function(data) { 
			    //var row ='"row_'+data['1']+'"';
        		document.getElementById('compteurArticle').innerHTML= data['0'];
        		document.getElementById('blocDepartementsPanier').innerHTML= data['1'];
        		//document.getElementById(row).innerHTML= data['4'];
                setInterval('refreshPage()', 1000);
			}
		});
	}
	function RemoveProductPanier1(product_id,option,idclient) {
		$.ajax({
			url: 'cart.php',
			type: 'GET',
			data: 'id_produit=' + product_id + '&option=' + option + '&idclient=' + idclient + '&action=remove',
		    dataType: "json",
			success: function(data) { 
			    //var row ='"row_'+data['1']+'"';
        		document.getElementById('compteurArticle').innerHTML= data['0'];
        		document.getElementById('blocDepartementsPanier').innerHTML= data['1'];
        		//document.getElementById(row).innerHTML= data['4'];
                setInterval('refreshPage()', 1000);
			}
		});
	}

	function RemoveBonReduction() {
		$.ajax({
			url: 'cart.php',
			type: 'GET',
			data: 'action=supp_coupon',
			success: function() { 	
              setInterval('refreshPage()', 1000);
			}
		});
	}
	</script>
	
	
	<div class="alert alert-success alert-dismissible mt-2" role="alert" id="myAlert" style="position: fixed; top: 0; right: 10px;z-index: 999999;display:none;">
        <strong class="mr-auto"> Panier</strong>
		<hr>
		<p class="mb-0"> Succès ! votre produit à été ajouté au panier. <a href="https://www.sotic.tn/panier/" class="alert-link" style="font-size: 0.9rem;float: right;text-decoration: underline;">Voir votre panier</a></p>
		
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>

	</div>
</head>
<body>
	
	   
	
	<div class="top-navbar">
		<div class="container-lg">
			
			<div class="d-flex flex-row align-items-center my-4 top-section">

			    <a class="navbar-brand" href=""><img src="media/site/logo-logo.webp" class="logo-navbar"></a>
				
				<div class="d-flex justify-content-center d-lg-none">
        		        <a href="https://www.sotic.tn/favoris/" class="cart-nav d-flex align-items-center me-2 pe-2">
        		            <img src="dist/images/heart.webp" class="img-fluid me-2" style="object-fit:contain">
        		            <div> FAVORIS <br> 
        		                <span id="blocWishList">0</span> produit(s)
        		            </div>
        		        </a>
        		        <a href="https://www.sotic.tn/panier/" class="cart-nav d-flex align-items-center me-2">
        		            <div class=" position-relative me-3">
        		                <img src="dist/images/cart_shop.webp" class="img-fluid" style="object-fit:contain">
        		            	<span class="position-absolute start-100 translate-middle badge rounded-pill"><span id="compteurArticle">0</span></span>
        		            </div>
        		            <div> VOTRE PANIER <br> 
    						        		                <span id="blocDepartementsPanier">0.000 DT</span>						
    						        		            </div>
        		        </a>
    		    </div>
						        
				<div class="w-sm-100 me-2" id="the-basics">

					<form method="POST" action="recherche/" enctype="multipart/form-data" novalidate="novalidate" id="form_search">    
						<div class="input-group flex-nowrap position-relative">
							<input type="text" class="typeahead form-control input-sm pac-target-input" value="" autocomplete="off" id="searchVal" name="search" aria-label="Text input with dropdown button" placeholder="Tapez votre recherche ...">
							
							<!-- In index.php, add this before the closing body tag -->
							<div id="spinner" style="display:none;background:#f8f8f8;"><img src="dist/img/loader.gif" width="45px" style="mix-blend-mode: darken;border-top: 1px solid #dbdbdb;border-bottom: 1px solid #dbdbdb;height: -webkit-fill-available;"></div>
							<button type="submit" class="btn input-group-addon">
								<i class="fas fa-search" style="transform: rotate(90deg);"></i>
							</button>
							<input type="hidden" name="action" value="search">							
						</div>
					</form>

					<script>
    document.getElementById('form_search').addEventListener('submit', function (event) {
        // Récupérer la valeur du champ de recherche
        const searchValue = document.getElementById('searchVal').value.trim();
        
        if (!searchValue) {
            // Si le champ est vide, empêcher la soumission et afficher un message
            event.preventDefault();
            alert('Veuillez entrer une recherche avant de soumettre.');
            return;
        }

        // Modifier dynamiquement l'attribut "action" du formulaire
        const form = this;
        form.action = `/recherche/${encodeURIComponent(searchValue)}/`;
    });
</script>


					<div id="searchDataList" class="position-absolute" style="display:none;z-index:999;width: 95%;left: 50%;transform: translate(-50%,0);aspect-ratio: 16/9;"></div>
				</div>
				
    				<div class="d-flex justify-content-center d-none d-lg-flex">
        		        <a href="https://www.sotic.tn/favoris/" class="cart-nav d-flex align-items-center me-2 pe-2">
        		            <img src="dist/images/heart.webp" class="img-fluid me-2" style="object-fit:contain">
        		            <div> FAVORIS <br> 
        		                <span id="blocWishList">0</span> produit(s)
        		            </div>
        		        </a>
        		        <a href="https://www.sotic.tn/panier/" class="cart-nav d-flex align-items-center me-2">
        		            <div class=" position-relative me-3">
        		                <img src="dist/images/cart_shop.webp" class="img-fluid" style="object-fit:contain">
        		            	<span class="position-absolute start-100 translate-middle badge rounded-pill"><span id="compteurArticle">0</span></span>
        		            </div>
        		            <div> VOTRE PANIER <br> 
    						        		                <span id="blocDepartementsPanier">0.000 DT</span>						
    						        		            </div>
        		        </a>
    		        </div>
		        <a href="tel:(+216) 58 58 13 27" class="btn btn-contact d-none d-lg-block">
		            Besoin de Renseignements ?<br/> (+216) 58 58 13 27		        </a>
	        </div>
		</div>
		
		<a href="tel:(+216) 58 58 13 27" class="btn btn-contact d-block mx-auto d-md-none" style="position: fixed;z-index: 999;bottom: 0;width: 100%;background: #066734;border-radius: 0px;color: #fff!important;">
		    <i class="fa fa-phone me-2"></i> Besoin de Renseignements ?<br/> (+216) 58 58 13 27		</a>
	    
	</div>
	
	<script>
		const searchInput = document.getElementById('searchVal');
		const resultsContainer = document.getElementById('searchDataList');
		let isClickInsideResults = false;
		let timeout = null; // Variable pour stocker le timeout

		searchInput.addEventListener('input', function() {
			clearTimeout(timeout);

            var query = this.value;
			timeout = setTimeout(() => {
			// Fonction AJAX pour envoyer la requête de recherche
			fetchResults(query);
			}, 500);
            

        });

		function fetchResults(query) {
		if (query.trim() === "") return; // Ne fais rien si le champ est vide

		document.getElementById('spinner').style.display = 'block';
            if (query.length > 2) {
                var xhr = new XMLHttpRequest();
                xhr.open('GET', 'search-file.php?q=' + query, true);
                xhr.onload = function() {
                    document.getElementById('spinner').style.display = 'none';
                    if (this.status === 200) {
                        resultsContainer.style.display = "block";
                        resultsContainer.innerHTML = this.responseText;
                    }
                };
                xhr.send();
            } else {
                resultsContainer.innerHTML = '';
                document.getElementById('spinner').style.display = 'none';
            }
		}

		// Masquer le conteneur de résultats
		function hideResults() {
		 if (!isClickInsideResults) { // Vérifie si le clic est dans les résultats
			resultsContainer.style.display = 'none';
		 }
		} 
		function showResults() {
			resultsContainer.style.display = 'block';
		}

		document.addEventListener('click', function(event) {
		if (!searchInput.contains(event.target) && !searchInput.contains(event.target)) {
		// Si le clic est en dehors du champ de recherche et du conteneur de résultats, masque le conteneur
		hideResults()
		}
		});

		// Détecte les clics dans le conteneur des résultats
		resultsContainer.addEventListener('mousedown', function() {
		    isClickInsideResults = true;
		});

		// Réinitialise la variable `isClickInsideResults` après le clic
		document.addEventListener('mouseup', function() {
		    isClickInsideResults = false;
		});

		// Masque les résultats si le champ de recherche perd le focus
		searchInput.addEventListener('blur', hideResults);

		// Masque les résultats si la fenêtre ou l'onglet devient inactif
		document.addEventListener('visibilitychange', function() {
		    if (document.visibilityState === 'hidden') {
		        hideResults();
		    }
		});
		// Affiche le conteneur de résultats si l'utilisateur clique dans le champ de recherche et qu'il y a des résultats
		searchInput.addEventListener('focus', function() {
		    if (resultsContainer.innerHTML.trim() !== '') {
		        resultsContainer.style.display = 'block';
		    }
		});

    </script>	
    
    <!-- site-mobile-menu -->
    
    <div class="site-mobile-menu site-navbar-target">
        <div class="site-mobile-menu-header">
            <div class="site-mobile-menu-close mt-3">
                <span class="icon-close2 js-menu-toggle"></span>
            </div>
        </div>
        <div class="site-mobile-menu-body"> </div>

		<a href="tel:(+216) 58 58 13 27" class="btn btn-contact d-block mx-auto">

		    Besoin de Renseignements ?<br/> (+216) 58 58 13 27
		</a>
    </div> 
    
    <!-- site-mobile-menu -->
	
	<!-- Nav-bar -->
        	
    <div class="site-navbar-wrap position-relative mt-4 mt-md-0">
       	<div class="site-navbar site-navbar-target ">
       		<div class="container-xxl container-fluid">
                <nav class="site-navigation text-end" role="navigation">
                              
                    <div class="d-inline-block d-lg-none me-md-0 ms-auto py-2">
						<a href="#" class="site-menu-toggle js-menu-toggle"><span class="icon-menu h3" style="vertical-align: sub;"></span></a>
					</div>
            
                    <ul class="site-menu main-menu js-clone-nav d-none d-lg-block">
						
												<li class="">
							<a href="https://www.sotic.tn/" class="nav-link" >
							    Accueil							</a>
                               						</li>

                        						<li class="">
							<a href="https://www.sotic.tn/qui-sommes-nous/" class="nav-link" >
							    Qui sommes nous ?							</a>
                               						</li>

                        						<li class="has-children">
							<a href="javascript:void(0)" class="nav-link" >
							    Notre catalogue							</a>
                               <ul class='dropdown arrow-top'><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/cloture-grillage/"'>Clôture & grillage</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/cloture-grillage/grillage-ondule/'>Grillage ondulé</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/cloture-grillage/grillage-simple-torsion/'>Grillage Simple Torsion</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/cloture-grillage/panneau-clr-33/'>Panneau Clr 33</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/cloture-grillage/poteaux-en-tole-forme-de-i/'>Poteaux En Tole Forme De I</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tole/"'>Tôle</span></a><ul class="dropdown arrow-top"><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tole/aluminium/"'>Aluminium</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tole/aluminium/tole-aluminium-larmee/'>Tôle Aluminium larmée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/aluminium/tole-aluminium/'>Tôle Aluminium</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tole/galvanisee/"'>Galvanisée</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tole/galvanisee/tole-nervuree-galvanisee/'>Tôle nervurée galvanisée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/galvanisee/tole-micro-nervuree-galvanisee/'>Tôle micro nervurée galvanisée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/galvanisee/tole-ondulee-galvanisee/'>Tôle ondulée galvanisée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/galvanisee/tole-plane-galvanisee/'>Tôle plane galvanisée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/galvanisee/caillebotis/'>Caillebotis</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/galvanisee/tole-micro-nerv-gal-martele/'>TOLE MICRO NERV GAL MARTELE</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tole/noir/"'>Noir</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tole/noir/tole-plane-noir-laf/'>Tôle plane noir LAF</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/noir/tole-plane-noir-lac/'>Tôle plane noir LAC</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/noir/tole-perforee/'>Tôle perforée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/noir/tole-larmee/'>Tôle larmée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/noir/tole-striee/'>Tôle striée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/noir/tole-trouee/'>Tôle trouée</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tole/inox/"'>Inox</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tole/inox/tole-trouee-2/'>Tôle trouée</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tole/inox/t-p-inox/'>T P INOX</a>
                                                         </li></ul></li><li>
                                                             <a class='nav-link' href='categories/tole/marine/'>Marine</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/panneau-sandwich/"'>Panneau Sandwich</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/panneau-sandwich/bardage/'>Bardage</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/panneau-sandwich/couverture/'>Couverture</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/fer-marchand/"'>Fer marchand</span></a><ul class="dropdown arrow-top"><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/fer-marchand/fer-rond/"'>FER ROND</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-rond/fer-rond-06-10/'>Fer rond 06----> 10</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-rond/fer-rond-11-20/'>Fer rond 11 ---->20</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-rond/fer-rond-22-35/'>Fer rond 22 ---- > 35</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-rond/fer-rond-36-50/'>Fer rond 36 ----> 50</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-rond/fer-rond-60-100/'>Fer rond 60 ----> 100</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/fer-marchand/corniere/"'>CORNIERE</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/fer-marchand/corniere/corniere-20-50/'>CORNIERE 20 ---> 50</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/corniere/corniere-60-90/'>CORNIERE 60 ---> 90</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/corniere/corniere-90/'>CORNIERE  >90</a>
                                                         </li></ul></li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-a-t/'>FER A T</a>
                                                         </li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/fer-marchand/fer-carre/"'>FER CARRE</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-carre/fer-carre-8-20/'>FER CARRE  8 ---->20</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-carre/fer-carre-25-50/'>FER CARRE  25 ----> 50</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-carre/fer-carre-60-100/'>FER CARRE  60 ----> 100</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/fer-marchand/fer-plat/"'>FER PLAT</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-plat/fer-plat-10-35/'>FER PLAT 10 ---> 35</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-plat/fer-plat-40-80/'>FER PLAT 40 ---> 80</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-plat/fer-plat-100-300/'>FER PLAT 100 ---> 300</a>
                                                         </li></ul></li><li>
                                                             <a class='nav-link' href='categories/fer-marchand/fer-uac/'>FER UAC</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/poutrelle/"'>Poutrelle</span></a><ul class="dropdown arrow-top"><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/poutrelle/fer-hea-heb/"'>FER HEA & HEB</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-hea-heb/fer-hea-heb-100-260/'>FER HEA /HEB  100 --->260</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-hea-heb/fer-hea-heb-280-400/'>FER HEA /HEB  280 --->400</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-hea-heb/fer-hea-heb-450-1000/'>FER HEA /HEB  450 ---> 1000</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/poutrelle/fer-ipe/"'>FER IPE</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-ipe/fer-ipe-80-160/'>FER IPE 80 --->160</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-ipe/fer-ipe-180-600/'>FER IPE 180 --->600</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-ipe/fer-ipe-aa/'>FER IPE AA</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-ipe/fer-ipe-aaa/'>FER IPE AAA</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/poutrelle/fer-upn/"'>FER UPN</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-upn/fer-upn-80-160/'>FER UPN 80 --->160</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-upn/fer-upn-180-400/'>FER UPN 180 --->400</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/poutrelle/fer-upn/fer-upn-aa/'>FER UPN AA</a>
                                                         </li></ul></li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tube/"'>Tube</span></a><ul class="dropdown arrow-top"><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tube/tube-laf/"'>Tube LAF</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tube/tube-laf/carre/'>CARRÉ</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tube/tube-laf/rectangulaire/'>RECTANGULAIRE</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tube/tube-laf/rond/'>ROND</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tube/tube-lac/"'>Tube LAC</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tube/tube-lac/carre-1/'>CARRÉ</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tube/tube-lac/rectangulaire-1/'>RECTANGULAIRE</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tube/tube-lac/rond-1/'>ROND</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tube/tube-inox/"'>Tube inox</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tube/tube-inox/carre-2/'>CARRÉ</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tube/tube-inox/rond-4/'>ROND</a>
                                                         </li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/tube/tube-galvanise/"'>Tube galvanisé</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/tube/tube-galvanise/carre-3/'>CARRÉ</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tube/tube-galvanise/rectangulaire-2/'>RECTANGULAIRE</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/tube/tube-galvanise/rond-2/'>ROND</a>
                                                         </li></ul></li></ul></li><li class='has-children'>
                                                      <a class='nav-link' href='javascript:void(0)'><span onclick='window.location="categories/accessoires-portes-rideaux-et-coulissantes/"'>Accessoires portes rideaux et coulissantes</span></a><ul class="dropdown arrow-top"><li>
                                                             <a class='nav-link' href='categories/accessoires-portes-rideaux-et-coulissantes/accessoires-portes-rideaux/'>Accessoires portes rideaux</a>
                                                         </li><li>
                                                             <a class='nav-link' href='categories/accessoires-portes-rideaux-et-coulissantes/accessoires-portes-coulissantes/'>Accessoires portes coulissantes</a>
                                                         </li></ul></li></ul>						</li>

                        						<li class="">
							<a href="https://www.sotic.tn/en-promo/" class="nav-link" >
							    En promo							</a>
                               						</li>

                        						<li class="">
							<a href="https://www.sotic.tn/nouveautes/" class="nav-link" >
							    Nouveautés							</a>
                               						</li>

                        						<li class="">
							<a href="https://www.sotic.tn/livraison/" class="nav-link" >
							    Livraison							</a>
                               						</li>

                        						<li class="">
							<a href="demande-devis/" class="nav-link" >
							    Devis en ligne							</a>
                               						</li>

                           
					</ul>
                    
				</nav>
            </div>
        </div>
    </div>
	<!-- Fin Nav-bar -->
	
		
	
	<section class="selection pb-3" id="section-selection">
		<div class="container-custom container-fluid">
		
		
		<section class="selection-breadcrumbs">
			<div class="container container-custom">
	<!---------------- Breadcrumb ----------------------->


                <div class="breadcrumbs py-3">	
                    <ol class="justify-content-start">
                        <li><i class="fa fa-home"></i> <a href="https://www.sotic.tn/">Accueil</a></li>
                        <li><a href="categories/ ">Catalogue</a></li>            			<li>fer a t</li>            			            			            			            			                    </ol>
                </div>	
	<!--------------- Fin Breadcrumb ----------------->
			</div>
		</section>
            
            
                        <h1 class="text-uppercase text-center mb-4">FER A T</h1>
                        
		</div>
	</section>
	


	
	<div class="main">
	
	
	
	
	
	<section class="bloc_accueil py-3">
        
        <div class="container container-custom">
        
            <div class="row">
        		
        		

    <div class="col-md-3 left-content mb-4 order-2 order-md-1">
        
        		<div class="shop_sidebar_area filter_area">
    		<div class="filter mb-3 rounded-3">
    			<h3> Filter</h3>
    		</div>
            
            <div class="shop_sidebar_area_section bg-white rounded-3" style="overflow:hidden">
    			
                <form action="recherche/" method="get" enctype="multipart/form-data">
                <!-- ##### Single Widget ##### -->
                <div class="widget brands">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4 py-3" style="color: #fff;background: #009949;">Catégories</h3>
					                    <!--  Catagories  -->
                    <div class="widget-desc">
                        
                                                </div>
                </div>
    
                <!-- ##### Single Widget ##### -->
                <div class="widget brands ">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4 py-3" style="color: #fff;background: #009949;">Marques</h3>
    
                    <div class="widget-desc">
                                                
                    </div>
                </div>
                
                
                <!-- ##### Single Widget ##### -->
                <div class="widget brands ">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4 py-3" style="color: #fff;background: #009949;">Type de profile</h3>
    
                    <div class="widget-desc">
                                                
                    </div>
                </div>
                
                <!-- ##### Single Widget ##### -->
                <div class="widget brands ">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4 py-3" style="color: #fff;background: #009949;">Forme</h3>
    
                    <div class="widget-desc">
                                                
                    </div>
                </div>
                
                
                <!-- ##### Single Widget ##### -->
                <div class="widget brands ">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4 py-3" style="color: #fff;background: #009949;">Stock</h3>
    
                    <div class="widget-desc">
                         					
                        <!-- Single Form Check -->
                        <div class="form-check px-4">
                            <input class="form-check-input common_selector stock_selector ms-auto" type="checkbox" name="stocks[]" value="2" id="s2" >
                            <label class="form-check-label ms-2" for="s2">En Précommande</label>
                        </div>
						<!-- Single Form Check -->
                        <div class="form-check px-4">
                            <input class="form-check-input common_selector stock_selector ms-auto" type="checkbox" name="stocks[]" value="1" id="s1" >
                            <label class="form-check-label ms-2" for="s1">En Stock</label>
                        </div>
						<!-- Single Form Check -->
                        <div class="form-check px-4">
                            <input class="form-check-input common_selector stock_selector ms-auto" type="checkbox" name="stocks[]" value="0" id="s0" >
                            <label class="form-check-label ms-2" for="s0">Hors Stock</label>
                        </div>
                        
                    </div>
                </div>
    

                <!-- ##### Single Widget ##### -->
                <div class="widget price ">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4 py-3 mb-4" style="color: #fff;background: #009949;">Prix</h3>
    
                    <div class="widget-desc">
                        <div class="slider-range px-4">
                            	
                            <div id="price_range" class="mb-3"></div>
        					<input type="hidden" id="hidden_minimum_price" name="minimum_price" value="0.000" />
                            <input type="hidden" id="hidden_maximum_price" name="maximum_price" value="1554.000" />
                            <p><label class="prix-label">Prix : </label> <span id="price_show">0.000 DT - 1554.000 DT</span></p>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-search mx-4">Rechercher</button>
					<input type="hidden" name="action" value="search">
                </div>
                
                </form>
                
            </div>
        
        </div>				        
								
    </div>        		
        		
        		
        		<div class="col-md-9 right-content order-1 order-md-2">
        		                    		
        		    
                						<div class="produits">
				<div class="py-4">
    				<h2>Produits : FER A T</h2>
    				<div class="divider"></div>
				</div>
				
				<div class="prod-content border-0 row position-relative">
				                
				                      
                                        											<div class="row " > 
																						<div class="col-md-12 row align-items-center sort-section justify-content-end mx-0 py-2">
												<div class="col-md-6 text-end">
													<select name="ordre" class="show-tick form-control sort" onchange="window.location=this.value;">
													    <option value="categories/fer-a-t/">Trier par</option>
													    <option value="categories/fer-a-t/sort/PRIX_ASC/" >Du moins cher au plus cher</option>
													    <option value="categories/fer-a-t/sort/PRIX_DESC/" >Du plus cher au moins cher</option>
													    <option value="categories/fer-a-t/sort/ALPHA_ASC/" >Ordre alphabétique Croissant</option>
													    <option value="categories/fer-a-t/sort/ALPHA_DESC/" >Ordre alphabétique Décroissant</option>
													</select>
												</div>  
											</div> 
																						            			                    <div class=" col-md-3 mt-2  gx-1 mb-3 produit-sc">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
																												<p class="bg-danger avaibility text-white p-2"> Hors stock</p>
																											</div>
                    							    
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/fer-marchand/fer-a-t/fer-t-25-x-25-x-3-5-x-6ml-g/" class="d-block h-100 w-100"><img src="media/products/468-produits-Fer-T-SOTIC.jpg" alt="" class="img-fluid"></a>
                    									<div class="position-absolute w-100 start-0 bottom-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 bottom-0 translate-middle ">
                        									    <a href="produit/fer-marchand/fer-a-t/fer-t-25-x-25-x-3-5-x-6ml-g/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlistm3cm468lsqp167lcy5">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlistm3cm468lsqp167lcy5"  onclick="addToWishList('m3cm468lsqp167lcy5');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="far fa-heart" aria-hidden="true"></i>
                            	                                    </button>
                                                                </div>
                                                                                    									    </div>    
                    									        
                    									</div>
                    								</div>
                    
                    									<!-- Product Meta Data -->
                    									<div class="product-meta-data">
                        									<!-- Ratings & Cart -->
                        									<div class="ratings-cart d-flex align-items-center justify-content-center">
                        									  	<div class="rating2" data-rateyo-rating="0" data-rateyo-num-stars="5"  data-rateyo-score="0"> </div>
															</div>
                    										<a href="produit/fer-marchand/fer-a-t/fer-t-25-x-25-x-3-5-x-6ml-g/" class="">
                    											<h3>Fer T  25 X 25 X 3.5 X 6ml- G</h3>
                    										</a>
                    										                        									<p class="product-price m-0">26.036 DT <span class="uniteProd"> /barre</span></p>
                        									                    									</div>
                    							</div>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-3 mt-2  gx-1 mb-3 produit-sc">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
																												<p class="bg-danger avaibility text-white p-2"> Hors stock</p>
																											</div>
                    							    
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/fer-marchand/fer-a-t/fer-t-30-x-30-x-4-0-x-6ml-g/" class="d-block h-100 w-100"><img src="media/products/467-produits-Fer-T-30-SOTIC.jpg" alt="" class="img-fluid"></a>
                    									<div class="position-absolute w-100 start-0 bottom-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 bottom-0 translate-middle ">
                        									    <a href="produit/fer-marchand/fer-a-t/fer-t-30-x-30-x-4-0-x-6ml-g/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlistdtk8467p4mimhpljid">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlistdtk8467p4mimhpljid"  onclick="addToWishList('dtk8467p4mimhpljid');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="far fa-heart" aria-hidden="true"></i>
                            	                                    </button>
                                                                </div>
                                                                                    									    </div>    
                    									        
                    									</div>
                    								</div>
                    
                    									<!-- Product Meta Data -->
                    									<div class="product-meta-data">
                        									<!-- Ratings & Cart -->
                        									<div class="ratings-cart d-flex align-items-center justify-content-center">
                        									  	<div class="rating2" data-rateyo-rating="0" data-rateyo-num-stars="5"  data-rateyo-score="0"> </div>
															</div>
                    										<a href="produit/fer-marchand/fer-a-t/fer-t-30-x-30-x-4-0-x-6ml-g/" class="">
                    											<h3>Fer T  30 X 30 X 4.0 X 6ml- G</h3>
                    										</a>
                    										                        									<p class="product-price m-0">38.706 DT <span class="uniteProd"> /barre</span></p>
                        									                    									</div>
                    							</div>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-3 mt-2  gx-1 mb-3 produit-sc">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
																												<p class="bg-lightgreen avaibility p-2" style="font-weight:400;font-size:12px"> En stock</p>
																											</div>
                    							    
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/fer-marchand/fer-a-t/fer-t-35-x-35-x-4-5-x-6ml/" class="d-block h-100 w-100"><img src="media/products/466-produits-Fer-T-35-SOTIC.jpg" alt="" class="img-fluid"></a>
                    									<div class="position-absolute w-100 start-0 bottom-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 bottom-0 translate-middle ">
                        									    <a href="produit/fer-marchand/fer-a-t/fer-t-35-x-35-x-4-5-x-6ml/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                									<button type="button" onclick="addToCart('2nbc466xbb43xkd56j', '1');" class="d-block cart-icone">
                            									    <img src="dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain">
                            									</button>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist2nbc466xbb43xkd56j">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist2nbc466xbb43xkd56j"  onclick="addToWishList('2nbc466xbb43xkd56j');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="far fa-heart" aria-hidden="true"></i>
                            	                                    </button>
                                                                </div>
                                                                                    									    </div>    
                    									        
                    									</div>
                    								</div>
                    
                    									<!-- Product Meta Data -->
                    									<div class="product-meta-data">
                        									<!-- Ratings & Cart -->
                        									<div class="ratings-cart d-flex align-items-center justify-content-center">
                        									  	<div class="rating2" data-rateyo-rating="0" data-rateyo-num-stars="5"  data-rateyo-score="0"> </div>
															</div>
                    										<a href="produit/fer-marchand/fer-a-t/fer-t-35-x-35-x-4-5-x-6ml/" class="">
                    											<h3>Fer T  35 X 35 X 4.5 X 6ml</h3>
                    										</a>
                    										                        									<p class="product-price m-0">49.855 DT <span class="uniteProd"> /barre</span></p>
                        									                    									</div>
                    							</div>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-3 mt-2  gx-1 mb-3 produit-sc">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
																												<p class="bg-danger avaibility text-white p-2"> Hors stock</p>
																											</div>
                    							    
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/fer-marchand/fer-a-t/fer-t-40-x-40-x-5-0-x-6ml-g/" class="d-block h-100 w-100"><img src="media/products/465-produits-Fer-T-40-SOTIC.jpg" alt="" class="img-fluid"></a>
                    									<div class="position-absolute w-100 start-0 bottom-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 bottom-0 translate-middle ">
                        									    <a href="produit/fer-marchand/fer-a-t/fer-t-40-x-40-x-5-0-x-6ml-g/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlistuk71465iisb3pjn3mh">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlistuk71465iisb3pjn3mh"  onclick="addToWishList('uk71465iisb3pjn3mh');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="far fa-heart" aria-hidden="true"></i>
                            	                                    </button>
                                                                </div>
                                                                                    									    </div>    
                    									        
                    									</div>
                    								</div>
                    
                    									<!-- Product Meta Data -->
                    									<div class="product-meta-data">
                        									<!-- Ratings & Cart -->
                        									<div class="ratings-cart d-flex align-items-center justify-content-center">
                        									  	<div class="rating2" data-rateyo-rating="0" data-rateyo-num-stars="5"  data-rateyo-score="0"> </div>
															</div>
                    										<a href="produit/fer-marchand/fer-a-t/fer-t-40-x-40-x-5-0-x-6ml-g/" class="">
                    											<h3>Fer T  40 X 40 X 5.0 X 6ml- G</h3>
                    										</a>
                    										                        									<p class="product-price m-0">58.886 DT <span class="uniteProd"> /barre</span></p>
                        									                    									</div>
                    							</div>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-3 mt-2  gx-1 mb-3 produit-sc">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
																												<p class="bg-lightgreen avaibility p-2" style="font-weight:400;font-size:12px"> En stock</p>
																											</div>
                    							    
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/fer-marchand/fer-a-t/fer-t-50-x-50-x-6-0-x-6ml/" class="d-block h-100 w-100"><img src="media/products/464-produits-Fer-T-50-SOTIC.jpg" alt="" class="img-fluid"></a>
                    									<div class="position-absolute w-100 start-0 bottom-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 bottom-0 translate-middle ">
                        									    <a href="produit/fer-marchand/fer-a-t/fer-t-50-x-50-x-6-0-x-6ml/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                									<button type="button" onclick="addToCart('6hkm464cxayd88i7e0', '1');" class="d-block cart-icone">
                            									    <img src="dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain">
                            									</button>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist6hkm464cxayd88i7e0">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist6hkm464cxayd88i7e0"  onclick="addToWishList('6hkm464cxayd88i7e0');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="far fa-heart" aria-hidden="true"></i>
                            	                                    </button>
                                                                </div>
                                                                                    									    </div>    
                    									        
                    									</div>
                    								</div>
                    
                    									<!-- Product Meta Data -->
                    									<div class="product-meta-data">
                        									<!-- Ratings & Cart -->
                        									<div class="ratings-cart d-flex align-items-center justify-content-center">
                        									  	<div class="rating2" data-rateyo-rating="0" data-rateyo-num-stars="5"  data-rateyo-score="0"> </div>
															</div>
                    										<a href="produit/fer-marchand/fer-a-t/fer-t-50-x-50-x-6-0-x-6ml/" class="">
                    											<h3>Fer T  50 X 50 X 6.0 X 6ml</h3>
                    										</a>
                    										                        									<p class="product-price m-0">96.236 DT <span class="uniteProd"> /barre</span></p>
                        									                    									</div>
                    							</div>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-3 mt-2  gx-1 mb-3 produit-sc">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
																												<p class="bg-danger avaibility text-white p-2"> Hors stock</p>
																											</div>
                    							    
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/fer-marchand/fer-a-t/fer-t-60-x-60-x-7-0-x-6ml-g/" class="d-block h-100 w-100"><img src="media/products/463-produits-Fer-T-50-SOTIC.jpg" alt="" class="img-fluid"></a>
                    									<div class="position-absolute w-100 start-0 bottom-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 bottom-0 translate-middle ">
                        									    <a href="produit/fer-marchand/fer-a-t/fer-t-60-x-60-x-7-0-x-6ml-g/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist5jri463yxhct9mhbh0">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist5jri463yxhct9mhbh0"  onclick="addToWishList('5jri463yxhct9mhbh0');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="far fa-heart" aria-hidden="true"></i>
                            	                                    </button>
                                                                </div>
                                                                                    									    </div>    
                    									        
                    									</div>
                    								</div>
                    
                    									<!-- Product Meta Data -->
                    									<div class="product-meta-data">
                        									<!-- Ratings & Cart -->
                        									<div class="ratings-cart d-flex align-items-center justify-content-center">
                        									  	<div class="rating2" data-rateyo-rating="0" data-rateyo-num-stars="5"  data-rateyo-score="0"> </div>
															</div>
                    										<a href="produit/fer-marchand/fer-a-t/fer-t-60-x-60-x-7-0-x-6ml-g/" class="">
                    											<h3>Fer T  60 X 60 X 7.0 X 6ml- G</h3>
                    										</a>
                    										                        									<p class="product-price m-0">128.358 DT <span class="uniteProd"> /barre</span></p>
                        									                    									</div>
                    							</div>
                    						</div>
                                    		
                		                    											</div>
											                		          
    		          </div>
				
				
			</div>
							
				
				        		
        		</div>
            	
        		

    <div class="col-md-12 full-content order-3">
				
                    </div>        		
		    
		    </div>
		    
		</div>
		
	</section>	
	    
        <div class="newsletter">
        <div class="container">
            <div class="d-flex align-items-center justify-content-between">
                <div class="d-flex newsletter-text-sc align-items-center justify-content-between me-3">
                    <img class="img-fluid me-4" src="dist/images/newsletter_icon.webp">
                    <div class="text-newsletter py-3">
                        <h3>Newsletter SOTIC</h3>
                        <h4>Abonnez-vous à notre lettre d'informations et restez informés des promotions et bons plans en exclusivité !</h4>
                    </div>
                </div>
                <form action="" method="post" id="contact-forms" class="mb-3 mb-md-0"  role="form" name="newsletter" onsubmit="return get_value1();">
                    <div class="input-group">
                        <input class="form-control newsletter-email" type="email" required  name="mail" id="email" placeholder="Votre adresse email...">
                        <button type="submit" class="btn bnt-abonner">S'abonner</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
	<footer class="footer pt-4">
		<div class="container container-custom">

			<div class="row">
			    
				<div class="col-lg-3 col-md-6 mb-4">
				    <a href="https://www.sotic.tn/" class="footer-img" > <img src="media/site/logo-logo.webp" class="img-fluid"> </a>
				    <div class="text-footer mt-3">
				        <p><font dir="auto" style="vertical-align:inherit"><font dir="auto" style="vertical-align:inherit">La soci&eacute;t&eacute; SOTIC, cr&eacute;&eacute;e en 1991, assure la commercialisation et la vente en gros et en d&eacute;tail d&#39;une large gamme de produits sid&eacute;rurgiques &amp; m&eacute;tallurgiques.</font></font></p>				    </div>
				</div>
				<div class="col-lg-3 col-md-6 mb-4 infos">
				    <h3>INFORMATIONS</h3>
				    <ul class="list-unstyled">
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="https://www.sotic.tn/qui-sommes-nous/">Qui sommes nous ?</a></li>
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="https://www.sotic.tn/livraison/">Livraison</a></li>
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="https://www.sotic.tn/conditions-generales-de-vente/">Conditions générales de vente</a></li>
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="contact/">Contactez-nous</a></li>
				        				    </ul>
				</div>
				<div class="col-lg-3 col-md-6 mb-4 infos">
				    <h3>NOTRE CATALOGUE</h3>
				    <ul class="list-unstyled">
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="categories/cloture-grillage/"> Clôture & grillage   </a></li>
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="categories/tole/"> Tôle   </a></li>
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="categories/panneau-sandwich/"> Panneau Sandwich   </a></li>
				        				        <li> <i class="fa fa-arrow-right me-1"></i><a href="categories/fer-marchand/"> Fer marchand   </a></li>
				        				    </ul>
				</div>
				<div class="col-lg-3 col-md-6 mb-4 infos">
				    <h3>SERVICE CLIENTS AU</h3>
				    <div class="service-cl-texte">
				        <img src="dist/images/phone_call_icon.webp" class="img-fluid">
				        (+216) 58 58 13 12				    </div>
					<div class="reseaux-sociaux p-3">
    					<div class="reseaux-sociaux-icones text-center">
					    <span>Réjoignez nous</span>
    			  	        				    <a href="https://www.facebook.com/profile.php?id=61553806449331"  target="_blank"><i class="fab fa-facebook-f"></i> </a>
    				        				    <a href="https://www.instagram.com/sotic_tunisie/"  target="_blank"><i class="fab fa-instagram"></i> </a>
    				        				    <a href="https://wa.me/58581330"  target="_blank"><i class="fab fa-whatsapp"></i> </a>
    				    				
    					</div>
					</div>
				</div>
			</div>
			
		</div>		
	</footer>
	<div class="pied-page text-center">
		<p>	
			Copyright © 2025 SOTIC. - Tous droits réservés.		</p>
	</div>
		<div class="wabtn" id="wabutton">
  <style> [wa-tooltip] { position: relative; cursor: default;  &:hover { &::before { content: attr(wa-tooltip); font-size: 16px; text-align: center; position: absolute; display: block; right: calc(0% - 100px); left: null; min-width: 200px; max-width: 200px; bottom: calc(100% + 10px); transform: translate(-50%); animation: fade-in 500ms ease; background: #00E785; border-radius: 4px; padding: 10px; color: #ffffff; z-index: 1; } } }  @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }  [wa-tooltip] {  }  @keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }</style>
  <a wa-tooltip="Nous sommes disponible! Clique ici pour discuter" target="_blank" href="https://wa.me/+21658581318?text=" style=" cursor: pointer;height: 62px;width: auto;padding: 10px 10px 10px 10px;position: fixed !important;color: #fff;bottom: 20px;right: 20px;;display: flex;font-size: 18px;font-weight: 600;align-items: center;z-index: 999999999 !important;background-color: #00E785;box-shadow: 4px 5px 10px rgba(0, 0, 0, 0.4);border-radius: 100px;animation: pulse 2.5s ease infinite;">
    <svg width="42" height="42" style="padding: 5px;" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1024_354)"><path d="M23.8759 4.06939C21.4959 1.68839 18.3316 0.253548 14.9723 0.0320463C11.613 -0.189455 8.28774 0.817483 5.61565 2.86535C2.94357 4.91323 1.10682 7.86244 0.447451 11.1638C-0.21192 14.4652 0.351026 17.8937 2.03146 20.8109L0.0625 28.0004L7.42006 26.0712C9.45505 27.1794 11.7353 27.7601 14.0524 27.7602H14.0583C16.8029 27.7599 19.4859 26.946 21.768 25.4212C24.0502 23.8965 25.829 21.7294 26.8798 19.1939C27.9305 16.6583 28.206 13.8682 27.6713 11.1761C27.1367 8.48406 25.8159 6.01095 23.8759 4.06939ZM14.0583 25.4169H14.0538C11.988 25.417 9.96008 24.8617 8.1825 23.8091L7.7611 23.5593L3.3945 24.704L4.56014 20.448L4.28546 20.0117C2.92594 17.8454 2.32491 15.2886 2.57684 12.7434C2.82877 10.1982 3.91938 7.80894 5.67722 5.95113C7.43506 4.09332 9.76045 2.87235 12.2878 2.48017C14.8152 2.08799 17.4013 2.54684 19.6395 3.78457C21.8776 5.02231 23.641 6.96875 24.6524 9.3179C25.6638 11.6671 25.8659 14.2857 25.2268 16.7622C24.5877 19.2387 23.1438 21.4326 21.122 22.999C19.1001 24.5655 16.6151 25.4156 14.0575 25.4157L14.0583 25.4169Z" fill="#E0E0E0"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6291 7.98363C10.3723 7.41271 10.1019 7.40123 9.85771 7.39143C9.65779 7.38275 9.42903 7.38331 9.20083 7.38331C9.0271 7.3879 8.8562 7.42837 8.69887 7.5022C8.54154 7.57602 8.40119 7.68159 8.28663 7.81227C7.899 8.17929 7.59209 8.62305 7.38547 9.11526C7.17884 9.60747 7.07704 10.1373 7.08655 10.6711C7.08655 12.3578 8.31519 13.9877 8.48655 14.2164C8.65791 14.4452 10.8581 18.0169 14.3425 19.3908C17.2382 20.5327 17.8276 20.3056 18.4562 20.2485C19.0848 20.1913 20.4843 19.4194 20.7701 18.6189C21.056 17.8183 21.0557 17.1323 20.9701 16.989C20.8844 16.8456 20.6559 16.7605 20.3129 16.5889C19.9699 16.4172 18.2849 15.5879 17.9704 15.4736C17.656 15.3594 17.4275 15.3023 17.199 15.6455C16.9705 15.9888 16.3139 16.7602 16.1137 16.9895C15.9135 17.2189 15.7136 17.2471 15.3709 17.0758C14.3603 16.6729 13.4275 16.0972 12.6143 15.3745C11.8648 14.6818 11.2221 13.8819 10.7072 13.0007C10.5073 12.6579 10.6857 12.472 10.8579 12.3007C11.0119 12.1472 11.2006 11.9005 11.3722 11.7003C11.5129 11.5271 11.6282 11.3346 11.7147 11.1289C11.7603 11.0343 11.7817 10.9299 11.7768 10.825C11.7719 10.7201 11.7409 10.6182 11.6867 10.5283C11.6001 10.3566 10.9337 8.66151 10.6291 7.98363Z" fill="white"></path><path d="M23.7628 4.02445C21.4107 1.66917 18.2825 0.249336 14.9611 0.0294866C11.6397 -0.190363 8.35161 0.804769 5.70953 2.82947C3.06745 4.85417 1.25154 7.77034 0.600156 11.0346C-0.051233 14.299 0.506321 17.6888 2.16894 20.5724L0.222656 27.6808L7.49566 25.7737C9.50727 26.8692 11.7613 27.4432 14.0519 27.4434H14.0577C16.7711 27.4436 19.4235 26.6392 21.6798 25.1321C23.936 23.6249 25.6947 21.4825 26.7335 18.9759C27.7722 16.4693 28.0444 13.711 27.5157 11.0497C26.9869 8.38835 25.6809 5.94358 23.7628 4.02445ZM14.0577 25.1269H14.0547C12.0125 25.1271 10.0078 24.5782 8.25054 23.5377L7.8339 23.2907L3.51686 24.4222L4.66906 20.2143L4.39774 19.7831C3.05387 17.6415 2.4598 15.1141 2.70892 12.598C2.95804 10.082 4.03622 7.72013 5.77398 5.88366C7.51173 4.04719 9.81051 2.84028 12.3089 2.45266C14.8074 2.06505 17.3638 2.5187 19.5763 3.74232C21.7888 4.96593 23.5319 6.89011 24.5317 9.21238C25.5314 11.5346 25.7311 14.1233 25.0993 16.5714C24.4675 19.0195 23.0401 21.1883 21.0414 22.7367C19.0427 24.2851 16.5861 25.1254 14.0577 25.1255V25.1269Z" fill="white"></path></g><defs><clipPath id="clip0_1024_354"><rect width="27.8748" height="28" fill="white" transform="translate(0.0625)"></rect></clipPath></defs></svg>
    <span class="button-text"></span>
  </a>
</div>
	
	</div>

	
    
    
    <script type="text/javascript">
        function addToWishList(code) {
              var favoris = "";
              var wishList = document.getElementById('wishlist'+code);
              var btnWishList = document.getElementById('btn-wishlist'+code);
              var blocWishList = document.getElementById('blocWishList');
              
              $.ajax({
                url: "ajax/addwishlist.php",
                type: "POST",
			    data: 'code=' + code ,
		        dataType: "json",
                success: function(data) {
                    btnWishList.innerHTML = '<i class="fa fa-heart" aria-hidden="true"></i>';
                    document.getElementById('blocWishList').innerHTML = data[0];
                    var codeP = "'"+code+"'";
                    $(wishList).html('<button type="button" class="d-block cart-icone-blue " id="btn-wishlist'+code+'" onclick="removeFromWishList('+codeP+');"  ><i class="fa fa-heart" aria-hidden="true"></i></button>');
                    //window.location.reload()
                }
              })
        }
        function removeFromWishList(code) {
              var favoris = "";
              var wishList = document.getElementById('wishlist'+code);
              var btnWishList = document.getElementById('btn-wishlist'+code);
              var blocWishList = document.getElementById('blocWishList');
              
              $.ajax({
                url: "ajax/removewishlist.php",
                type: "POST",
			    data: 'code=' + code ,
		        dataType: "json",
                success: function(data) {
                    
                    btnWishList.innerHTML = '<i class="far fa-heart" aria-hidden="true"></i>';
                    document.getElementById('blocWishList').innerHTML = data[0];
                    var codeP = "'"+code+"'";
                    $(wishList).html('<button type="button" class="d-block cart-icone-blue " id="btn-wishlist'+code+'" onclick="addToWishList('+codeP+');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris"><i class="far fa-heart" aria-hidden="true"></i></button>');
                    //window.location.reload()
                }
              })
        }
    </script>
    <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MFGP3PBZ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->   

  	<script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.6.0/slick.js"></script>  
  	
  
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
  
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    
	
    <script src="assets/vendor/aos/aos.js"></script>
    
    <script src="assets/vendor/php-email-form/validate.js"></script>
    
    <!-- All js plugins included in this file. -->
    <script src="dist/js/plugins.js"></script>
    
    <!-- Main js file that contents all jQuery plugins activation. -->
    <script src="dist/js/main.js"></script>
	
    <script src="dist/js/jquery.sticky.js"></script>
    <script src="dist/js/mobile-js.js"></script>
	
	<!-- Typehead Plugin JavaScript -->
    <script src="dist/js/typeahead.js"></script>
    
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
	
	<script type="text/javascript">
		$(document).ready(function(){
			$('.products-home-box').slick({
			    rows: 2,
				infinite: true,
				slidesPerRow: 4,
                arrows: true,
        		prevArrow: '<div class="btn-case me-5"><i class="fa fa-angle-left  btn-carousel"></i></div>',
        		nextArrow: '<div class="btn-case"><i class="fa fa-angle-right  btn-carousel"></i></div>',
				pauseOnHover: false,
				responsive: [{
					breakpoint: 992,
					settings: {
						slidesPerRow: 2
					}
				}, {
					breakpoint: 768,
					settings: {
						slidesPerRow: 2
					}
				}, {
					breakpoint: 520,
					settings: {
						slidesPerRow: 1
					}
				}]
			});
			$('.categ-box').slick({
				slidesToShow: 4,
				slidesToScroll: 1,
				autoplay: true,
				autoplaySpeed: 2500,
				arrows: true,
				dots: false,
        		prevArrow: '<img src="dist/images/left-arrow.png" class="img-fluid slick-prev slick-grey"><img src="dist/images/left-arrow-orange.png" class="img-fluid slick-prev slick-orange">',
        		nextArrow: '<img src="dist/images/right-arrow.png" class="img-fluid slick-next slick-grey"><img src="dist/images/right-arrow-orange.png" class="img-fluid slick-next slick-orange">',
				pauseOnHover: false,
				responsive: [{
					breakpoint: 992,
					settings: {
						slidesToShow: 3
					}
				}, {
					breakpoint: 768,
					settings: {
						slidesToShow: 2
					}
				}, {
					breakpoint: 520,
					settings: {
						slidesToShow: 2
					}
				}]
			});
			$('.marque-box').slick({
				slidesToShow: 6,
				slidesToScroll: 1,
				autoplay: true,
				arrows: true,
				dots: false,
				prevArrow: '<div class="btn-case me-5"><i class="fa fa-angle-left  btn-carousel"></i></div>',
        		nextArrow: '<div class="btn-case"><i class="fa fa-angle-right  btn-carousel"></i></div>',
				pauseOnHover: false,
				responsive: [{
					breakpoint: 992,
					settings: {
						slidesToShow: 5
					}
				}, {
					breakpoint: 768,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 3
					}
				}, {
					breakpoint: 520,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 2
					}
				}]
			});
			
			
			$('.prod-box').slick({
			    rows: 4,
				infinite: true,
				slidesPerRow: 3,
                arrows: true,
				autoplay: false,
				dots: false,
				prevArrow: '<div class="btn-case me-5"><i class="fa fa-angle-left  btn-carousel"></i></div>',
        		nextArrow: '<div class="btn-case"><i class="fa fa-angle-right  btn-carousel"></i></div>',
				pauseOnHover: false,
				responsive: [{
					breakpoint: 992,
					settings: {
						slidesPerRow: 3
					}
				}, {
					breakpoint: 768,
					settings: {
						slidesPerRow: 2
					}
				}, {
					breakpoint: 520,
					settings: {
						slidesPerRow: 1
					}
				}]
			});
			$('.box-tablist').slick({
			    rows: 3,
				infinite: true,
				slidesPerRow: 3,
                arrows: true,
				autoplay: false,
				prevArrow: '<div class="btn-case me-5"><i class="fa fa-angle-left  btn-carousel"></i></div>',
        		nextArrow: '<div class="btn-case"><i class="fa fa-angle-right  btn-carousel"></i></div>',
				responsive: [{
					breakpoint: 992,
					settings: {
						slidesPerRow: 3
					}
				}, {
					breakpoint: 768,
					settings: {
						slidesPerRow: 2
					}
				}, {
					breakpoint: 520,
					settings: {
						slidesPerRow: 2
					}
				}]
			});
			$('a[data-bs-toggle="tab"]').on('shown.bs.tab', function(e) {
				$('.box-tablist').slick('setPosition');
			});
						
			$('.prod-sim-box').slick({
				slidesToShow: 3,
				slidesToScroll: 1,
				autoplay: false,
				arrows: true,
				dots: false,
				prevArrow: '<div class="btn-case me-5"><i class="fa fa-angle-left  btn-carousel"></i></div>',
        		nextArrow: '<div class="btn-case"><i class="fa fa-angle-right  btn-carousel"></i></div>',
				pauseOnHover: false,
				responsive: [{
					breakpoint: 992,
					settings: {
						slidesToShow: 3
					}
				}, {
					breakpoint: 768,
					settings: {
						slidesToShow: 2
					}
				}, {
					breakpoint: 520,
					settings: {
						slidesToShow: 1
					}
				}]
			});
		});

	</script>
	
	<script src="https://cdnjs.cloudflare.com/ajax/libs/rateYo/2.3.2/jquery.rateyo.min.js"></script>
	
	<script type="text/javascript">
	
    
        $(function () {
            $(".rating2").rateYo({
                normalFill: "#cbcbcb",
                ratedFill: "#ffc107",
                starWidth: "20px",
                readOnly: true
            });
            $("#rating2").rateYo({
                normalFill: "#cbcbcb",
                ratedFill: "#ffc107",
                starWidth: "20px",
                readOnly: true
            });
            $("#rating").rateYo({
                starWidth: "20px",
                normalFill: "#cbcbcb",
                ratedFill: "#ffc107"
            });
            $("#rating").rateYo().on("rateyo.change", function (e, data) {
                var rating = data.rating;
                $(this).parent().find('.score').text('score :'+ $(this).attr('data-rateyo-score'));
                $(this).parent().find('.result').text(rating);
                $(this).parent().find('input[name=rating]').val(rating); //add rating value to input field
            });
        });
			$(document).ready(function(){

            	$(window).scroll(function () {

            			if ($(this).scrollTop() > 50) {

            				$('#scrollUP').fadeIn();

            			} else {

            				$('#scrollUP').fadeOut();

            			}

            		});

            		// scroll body to 0px on click

            		$('#scrollUP').click(function () {

            			$('body,html').animate({

            				scrollTop: 0

            			}, 400);

            			return false;

            		});

            });

			

	</script>

	<script src="dist/js/zoomsl.js"></script>
    <script type="text/javascript">
		$(document).ready(function () {
			$('.myImage').imagezoomsl({ 
			zoomrange: [3, 3],
			magnifiersize: [640, 480],
			magnifierpos: "right"		
			
			/*,magnifierborder:'none'*/ 
			
			});
		});
	</script>



                <script>
                
            		$(document).ready(function () {
                        var qteID   = document.getElementById('qty');
                        var qte   = document.getElementById('qty').value;
            		    qteID.addEventListener("change", (event) => {
			                var idopt = $('#formCart input:checked').val();
                            qte = event.target.value;
                            $.post('ajax/price_values.php',{ idopt : idopt,qte:qte },
                            function(data){ 
                                document.getElementById('priceValue').innerHTML = data;
                                document.getElementById('qty').value= qte;
                            });
							$.post('ajax/eco_price.php',{ idopt : idopt,qte:qte },
                            function(data){ 
                                document.getElementById('priceValue').innerHTML = data;
                                document.getElementById('qty').value= qte;
                            });
                        });
            		});
            		
                    function selectOptionValues(value){
                        var idopt  = value;
                        var qteID  = document.getElementById('qty');
                        var code   = document.getElementById('codeProduct').value;
                        var qte    = document.getElementById('qty').value;
                        qteID.addEventListener("change", (event) => {
                            qte = event.target.value;
                        });
                        $.post('ajax/price_values.php',{ idopt : idopt,qte:qte },
                            function(data){ 
                                document.getElementById('priceValue').innerHTML = data;
                                document.getElementById('qty').value= qte;
                            }
                        );

                        $.post('ajax/get_qty.php',{ idopt : idopt },
                            function(data){ 
                                document.getElementById('qtydispo').value=data;
                            }
                        );
                        
                        $.post('ajax/qte_values.php',{ idopt : idopt },
                            function(data){ 
                                document.getElementById('stock').innerHTML = data;
                                if(data!=""){
                                var res = data.includes("rupture");
                                if (res) validate(0);
                                else validate(1);
                            }else validate(0);
                            }
                        );

                        $.post('ajax/get_ref_option.php',{ idopt : idopt,code:code },
                            function(data){ 
                                document.getElementById('refp').innerHTML = data;
                            }
                        );
                    }
                    
                </script>
	
	

 	 
 	 
 	 


    <!-- Modal -->
    <div class="modal fade" id="bank" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="bankLabel" aria-hidden="true" style="font-family: 'Montserrat';">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="bankLabel">Paiement par virement bancaire</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h5>Vous n&rsquo;avez pas de carte Bancaire ou Postale&nbsp;? Ce n&rsquo;est pas un soucis&nbsp;!</h5>

<p>Vous pouvez passer votre commande, en suivant les &eacute;tapes suivantes :</p>

<p style="margin-left:8px">1. Effectuez un versement ou un virement bancaire dans le compte avec les coordonn&eacute;es si-dessous.</p>

<p style="margin-left:8px">2. Envoyez le justificatif de paiement &agrave;&nbsp;<a href="mailto:Offre@sotic.tn" style="color:#1155cc" target="_blank">Offre@sotic.tn</a>&nbsp;avec votre Nom, Pr&eacute;nom ,N&deg;de t&eacute;l&eacute;phone et adresse email&nbsp;; ainsi que le Nom,Pr&eacute;nom et adresse email du b&eacute;n&eacute;ficiaire de la commande si ce n&rsquo;est&nbsp;pas&nbsp;pour vous</p>

<h5>NOS COORDONN&Eacute;ES BANCAIRES :</h5>

<p><strong>Banque :</strong>&nbsp;Attijari BANK Hammam Lif<br />
<strong>RIB:&nbsp;</strong>04007008404700354875</p>

<h6>Pour toute demande d&rsquo;information, n&rsquo;h&eacute;sitez pas &agrave; nous contacter au +216&nbsp;58 581 312.</h6>          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
          </div>
        </div>
      </div>
    </div>
	
		
	
 	<script type="text/javascript">
 	
    $(document).ready(function(){

        $('#price_range').slider({
            range:true,
            min:0.000,
            max:1554.000,
            values:[0.000, 1554.000],
            format:"DT",
            step:0.001,
            unit:'DT',
            stop:function(event, ui)
            {
                $('#price_show').html(ui.values[0] + ' DT - ' + ui.values[1] +' DT');
                $('#hidden_minimum_price').val(ui.values[0]);
                $('#hidden_maximum_price').val(ui.values[1]);
                //filter_data();
            }
        });

    });
    
    </script>

</body>
</html>
    """

class TestProductListDetectorForRealData:
    def setup_method(self):
        self.detector = ProductListExtractor()
    
    def test_sotic_tn(self):
        html = sotic_tn_products_page()
        result = self.detector.detect(html=html, page_url="https://www.sotic.tn/categories/fer-a-t/")
        assert result.is_product_list is True
        print(result.confidence_score)
        print(result.products)