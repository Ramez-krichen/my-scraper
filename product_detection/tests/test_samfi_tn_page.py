from product_detection import ProductListExtractor

def samfi_tn_products_page():
    return """
    
<!DOCTYPE html>
<html lang="en">
<head>

	

    <base href="https://www.samfi.tn/fr/"> 
  	
  		<!-- Required meta tags -->    
	
	
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" sizes="16x16" href="../media/site/favicon-favicon-samfi.png">    
        
    <title>Fer marchand</title>
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="ONLYTECH">
        <meta property="og:title" content="Fer marchand" />
    <meta property="og:description" content="" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://www.samfi.tn/fr/" />
    <meta property="og:image" content="https://www.samfi.tn/media/site/logo-logo-samfi.png" />
     
      	
  	<!-- Custom Font awesome -->
    <link rel="stylesheet" href="../dist/fontawesome-free-6.5.1-web/css/all.min.css">
    <link rel="stylesheet" href="../dist/font-awesome-4.7.0/css/font-awesome.min.css">
    
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

    <link rel="stylesheet" href="../dist/css/style.css" />
	
	<link rel="stylesheet" href="../dist/css/jquery-ui.min.css" />

    <link href="../assets/vendor/aos/aos.css" rel="stylesheet">
    
    <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
    
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
		<head>
    <style>
        body {
            position:relative;
            background-color: #f5f5f5;
            background-image: url(../dist/images/b_2.jpg),url(../dist/images/b_2_inv.jpg);
            background-repeat-x: no-repeat;
            background-size: contain,contain;
            background-blend-mode: color-burn,color-burn;
        }
        .navbar:after {
            content: "";
            background-image: url(../dist/images/bg-top.png);
            background-repeat: no-repeat;
            background-position: top center;
            background-size: 100% auto;
            position: absolute;
            display: block;
            top: 100%;
            bottom: 0;
            width: 100%;
            height: 300px;
            pointer-events: none;
            z-index: 1;
            opacity: 0.2;
        }
        .full-content .prod-content .product-img, .right-content .prod-content .product-img, .tablist-content .product-img {
            position:relative;
        }
        .full-content .prod-content .product-img:before, .right-content .prod-content .product-img:before, .tablist-content .product-img:before {
            content: "";
            background-image: url(../dist/images/OS5M9K1.png);
            background-repeat: no-repeat;
            background-position: left center;
            background-size: 100% auto;
            opacity: 0.2;
            left: 0;
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: #fff;
            background-blend-mode: luminosity;
        }
        .full-content .prod-content .product-img img, .right-content .prod-content .product-img img, .tablist-content .product-img img {
            mix-blend-mode: darken;
        }
		.top-navbar .top-section {
			margin-top: 1rem!important;
			margin-bottom: 0rem!important;
		}
        .left-content .service-content,.left-content .prod-content{ position:relative; z-index: 1; }
        .left-content .service-content:after,.left-content .prod-content:after {
            content: "";
            background-image: url("../dist/images/f1.png");
            background-repeat: no-repeat;
            background-position: top right;
            background-size: 20%;
            position: absolute;
            display: block;
            top: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 2;
            opacity: 0.5;
        }
        .left-content .service-content>div,.left-content .prod-content>div{ z-index: 3;}
        .left-mega-menu:after {
            content: "";
            background-image: url("../dist/images/f1.png");
            background-repeat: no-repeat;
            background-position: top right;
            background-size: 30%;
            position: absolute;
            display: block;
            top: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            opacity: 0.5;
        }
        .top-navbar {
            background-color: #003ca6;
            color: #fff;
            background-image: url(../dist/images/f11.png);
            background-position: bottom right;
            background-size: 70%;
            background-blend-mode: multiply;
            position:relative;
            background-repeat: repeat-x; 
        }
        .navbar-brand {
            position: relative;
            display: block;
            overflow: visible;
            height: 120px;
        }
        .navbar-brand:after {
            content: "";
            background-image: url("../dist/images/OS5M9K1.png");
            background-repeat: no-repeat;
            background-position: top center;
            position: absolute;
            background-size: contain;
            top: 6px;
            left: 10%;
            width: 100%;
            max-width: 100%;
            height: 100%;
            pointer-events: none;
        }
        .footer {
            background-color: #fff;
            position:relative;
        }
        .footer:after {
			content: "";
			background: url(../dist/images/f12.png) no-repeat bottom center;
			background-size: contain;
			width: 100%;
			max-width: 100%;
			height: 100%;
			display: block;
			position: absolute;
			bottom: 0;
			opacity: 0.3;
			z-index: 1;
		}
		.footer>div{ z-index: 2; }
        .prod-row {
            background-color: #f9bd12;
            border-radius: 10px;
            align-items: center;
            background-image: url(../dist/images/motif-ramadan.png);
            background-size: contain;
            background-blend-mode: multiply;
            position: relative;
            z-index: 1;
        }
        .prod-row:before {
            content: "";
            background-image: url("../dist/images/f.png");
            background-repeat: no-repeat;
            background-position: top left;
            background-size: contain;
            position: absolute;
            display: block;
            top: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 2;
            opacity: 0.5;
        }
        .prod-row:after {
            content: "";
            background-image: url("../dist/images/f1.png");
            background-repeat: no-repeat;
            background-position: top right;
            background-size: contain;
            position: absolute;
            display: block;
            top: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 2;
            opacity: 0.5;
        }
        .prod-row .slick-list{ z-index: 3; }
        @media screen and (max-width:524px){
            .navbar-brand {
                max-width: 180px;
            }
        }
    </style>
</head>
	
	<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MW89PM3S');</script>
<!-- End Google Tag Manager -->

 <script>
  fbq('track', 'Purchase');
</script>
 <script type="text/javascript">
(function() {
    window.sib = {
        equeue: [],
        client_key: "sm99rfxz881iib9cple2pfa9"
    };
    /* OPTIONAL: email for identify request*/
    // window.sib.email_id = 'example@domain.com';
    window.sendinblue = {};
    for (var j = ['track', 'identify', 'trackLink', 'page'], i = 0; i < j.length; i++) {
    (function(k) {
        window.sendinblue[k] = function() {
            var arg = Array.prototype.slice.call(arguments);
            (window.sib[k] || function() {
                    var t = {};
                    t[k] = arg;
                    window.sib.equeue.push(t);
                })(arg[0], arg[1], arg[2], arg[3]);
            };
        })(j[i]);
    }
    var n = document.createElement("script"),
        i = document.getElementsByTagName("script")[0];
    n.type = "text/javascript", n.id = "sendinblue-js", n.async = !0, n.src = "https://sibautomation.com/sa.js?key=" + window.sib.client_key, i.parentNode.insertBefore(n, i), window.sendinblue.page();
})();
</script>
 <!-- HTML Meta Tags -->
<title>Samfi Société Articles métalliques & fournitures industrielles</title>
<meta name="description" content="vente en ligne des équipements de soudure matériels et équipements d'atelier et industrielle   équipements de sécurités matériel de manutention et de levage soudage plastiques, et de fournitures SIDÉRURGIQUE">

<!-- Facebook Meta Tags -->
<meta property="og:url" content="https://www.samfi.tn/fr">
<meta property="og:type" content="website">
<meta property="og:title" content="Samfi Société Articles métalliques & fournitures industrielles">
<meta property="og:description" content="vente en ligne des équipements de soudure matériels et équipements d'atelier et industrielle   équipements de sécurités matériel de manutention et de levage soudage plastiques, et de fournitures SIDÉRURGIQUE">
<meta property="og:image" content="https://opengraph.b-cdn.net/production/images/18fc728a-eef2-4719-b13c-3669910c8ee7.png?token=VfHxj-ubPn_lshEY5rgrAARkXWbb6MKxiqUp2Hoy-ww&height=314&width=600&expires=33261893502">

<!-- Twitter Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta property="twitter:domain" content="samfi.tn">
<meta property="twitter:url" content="https://www.samfi.tn/fr">
<meta name="twitter:title" content="Samfi Société Articles métalliques & fournitures industrielles">
<meta name="twitter:description" content="vente en ligne des équipements de soudure matériels et équipements d'atelier et industrielle   équipements de sécurités matériel de manutention et de levage soudage plastiques, et de fournitures SIDÉRURGIQUE">
<meta name="twitter:image" content="https://opengraph.b-cdn.net/production/images/18fc728a-eef2-4719-b13c-3669910c8ee7.png?token=VfHxj-ubPn_lshEY5rgrAARkXWbb6MKxiqUp2Hoy-ww&height=314&width=600&expires=33261893502">

<!-- Meta Tags Generated via https://www.opengraph.xyz -->
 <script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "mbw8wxe4b1");
</script></script> <!-- Messenger Plugin de discussion Code -->
    <div id="fb-root"></div>

    <!-- Your Plugin de discussion code -->
    <div id="fb-customer-chat" class="fb-customerchat">
    </div>

    <script>
      var chatbox = document.getElementById('fb-customer-chat');
      chatbox.setAttribute("page_id", "110845593708146");
      chatbox.setAttribute("attribution", "biz_inbox");
    </script>

    <!-- Your SDK code -->
    <script>
      window.fbAsyncInit = function() {
        FB.init({
          xfbml            : true,
          version          : 'v18.0'
        });
      };

      (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = 'https://connect.facebook.net/fr_FR/sdk/xfbml.customerchat.js';
        fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'facebook-jssdk'));
    </script> <!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1023249425618832');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1023249425618832&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code --> <meta name="google-site-verification" content="qn1Qgssapv_lBys9mNE4-JO-wL-q0b_mYOUKcHTkg44" /> 
<meta name="msvalidate.01" content="3C70C59F150B7BE4A25BA05DE372B504" />	
			
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
		<p class="mb-0"> Succès ! votre produit à été ajouté au panier. <a href="https://www.samfi.tn/fr/panier/" class="alert-link" style="font-size: 0.9rem;float: right;text-decoration: underline;">Voir votre panier</a></p>
		
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>

	</div>
</head>
<body>
	
	
    

    <div class="topheader">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6">
                    <span class="slogan">Société articles métalliques & fournitures industrielles</span>
                </div>
                <div class="col-md-6">
                    <div class="d-flex align-items-center justify-content-end topheader-infos">
                        <span class="border-end pe-2 me-2 commande"><a href="tel:58581312"> COMMANDER AU <span>58581312</span> </a></span>
                        <span class="border-end pe-2 me-2 suivez-nous">
                            NOUS SUIVRE sur 
                                    				    <a href="https://fr-fr.facebook.com/SAMFI.TUNISIE/"  target="_blank" class="text-decoration-none"><i class="fa fa-facebook me-1"></i> </a>
        				            				    <a href="https://www.instagram.com/samfi_tunisie/"  target="_blank" class="text-decoration-none"><i class="fa fa-instagram me-1"></i> </a>
        				            				    <a href="https://tn.linkedin.com/company/samfitn"  target="_blank" class="text-decoration-none"><i class="fa fa-linkedin me-1"></i> </a>
        				            				    <a href="https://wa.me/58581324"  target="_blank" class="text-decoration-none"><i class="fa fa-whatsapp me-1"></i> </a>
        				            				    <a href="https://www.youtube.com/@Samfi-Tunisie"  target="_blank" class="text-decoration-none"><i class="fa fa-youtube-play me-1"></i> </a>
        				                            </span>
                        		            </div>
                </div>
            </div>
        </div>
    </div>
        
	<div class="top-navbar py-3">
		<div class="container">
			
			<div class="d-flex flex-row align-items-center my-4 top-section">

			    <a class="navbar-brand" href=""><img src="../media/site/logo-logo-samfi.png" class="logo-navbar"></a>
								<div  class="w-100 mx-3" id="the-basics">
					<form method="GET" action="recherche/" enctype="multipart/form-data" novalidate="novalidate" id="form_search">    
						<div class="input-group flex-nowrap position-relative">
							<input type="text" class="typeahead form-control input-sm pac-target-input" value="" autocomplete="off" id="searchVal" name="search" aria-label="Text input with dropdown button" placeholder="De quoi avez-vous besoin ?">
							
							<!-- In index.php, add this before the closing body tag -->
							<div id="spinner" style="display:none;"><img src="../dist/img/loader.gif" width="45px"></div>
							<button type="submit" class="btn p-0 border-0">
								<i class="fa fa-search input-group-text"></i>
							</button>
							<input type="hidden" name="action" value="search">							
						</div>
					</form>
					<div id="searchDataList" class="position-absolute" style="display:none;z-index:20;width: 95%;left: 50%;transform: translate(-50%,0);aspect-ratio: 16/9;"></div>
						
				</div>
				
				<div class="d-flex">
    		        <a href="https://www.samfi.tn/fr/favoris/" class="cart-nav d-flex border-end align-items-center me-2 pe-2" style="width:120px">
    		            <img src="../dist/images/heart.png" class="img-fluid me-2" style="object-fit:contain">
    		            <div> FAVORIS <br> 
    		                <span id="blocWishList" style="color: #ff7c48;font-weight: 600;">0</span> produit(s)
    		            </div>
    		        </a>
    		        <a href="https://www.samfi.tn/fr/panier/" class="cart-nav d-flex align-items-center" style="width:140px">
    		            <div class=" position-relative me-3">
    		                <img src="../dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain">
    		            	<span class="position-absolute start-100 translate-middle badge rounded-pill"><span id="compteurArticle">0</span></span>
    		            </div>
    		            <div> VOTRE PANIER <br> 
						    		                <span id="blocDepartementsPanier">0.000 DT</span>						
						    		            </div>
    		        </a>
		        </div>
	        </div>
		</div>
	    
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
	<!---------------- Nav-bar ----------------------->
	<nav class="navbar navbar-expand-lg navbar-light pt-3">
		<div class="container container-custom">

			<button class="navbar-toggler"  data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" type="button" aria-expanded="false" aria-controls="navbarSupportedContent">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="header-section">	

				<div class="navbar-collapse collapse" id="navbarSupportedContent">

					<ul class="navbar-nav mx-auto">
						
												   <li class="nav-item " >
							<a class="nav-link "  href="javascript:void(0)" >
							    <span onclick="window.location='la-societe/'">La société							    							    </a>
                               						</li>
						   
                        						   <li class="nav-item dropdown" >
							<a class="nav-link  dropdown-toggle "  href="javascript:void(0)"  role="button" data-bs-toggle="dropdown" aria-expanded="false" id="levelDropdownMenu2" >
							    <span onclick="window.location='categories/'">Nos produits							    							    <i class="fa fa-angle-down ms-1"></i>
							    <span class="sr-only">(current)</span>
							    							    </a>
                               <ul class='dropdown-menu'><li class='nav-item dropdown'>
                                                      <a class='dropdown-item dropdown-toggle' data-toggle='dropdown' href='javascript:void(0)'><span onclick='window.location="categories/soudure-accessoires/"'>Soudure & accessoires</span></a><ul class="dropdown-menu dropdown-submenu"><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudure-accessoires/consommables-de-soudure/'>Consommables de soudure</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudure-accessoires/equipements-de-soudure/'>Équipements de Soudure</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudure-accessoires/chalumeaux-et-detenteurs/'>chalumeaux et détenteurs</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudure-accessoires/accessoires-de-soudure/'>Accessoires de soudure</a>
                                                         </li></ul></li><li class='nav-item dropdown'>
                                                      <a class='dropdown-item dropdown-toggle' data-toggle='dropdown' href='javascript:void(0)'><span onclick='window.location="categories/outillages-equipements/"'>Outillages & équipements</span></a><ul class="dropdown-menu dropdown-submenu"><li class='nav-item dropdown'>
                                                      <a class='dropdown-item dropdown-toggle' data-toggle='dropdown' href='javascript:void(0)'><span onclick='window.location="categories/outillages-equipements/outils-electroportatifs/"'>Outils électroportatifs</span></a><ul class="dropdown-menu dropdown-submenu"><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/outils-electroportatifs/bosch/'>Bosch</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/outils-electroportatifs/hikoki/'>hikoki</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/outils-electroportatifs/skil/'>SKIL</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/outils-electroportatifs/offre-exclusif/'>Offre Exclusif</a>
                                                         </li></ul></li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/compresseur-secheurs/'>Compresseur & sécheurs</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/equipement-industriel/'>Equipement Industriel</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/nettoyeur-et-aspirateur/'>Nettoyeur et aspirateur</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/divers-accessoires/'>Divers Accessoires</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/outils-de-jardin/'>Outils de Jardin</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/bricolage-multi-usage/'>Bricolage Multi usage</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/equipement-de-chantier/'>Equipement de chantier</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/chargeur-demarreur-batterie/'>Chargeur & démarreur Batterie</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillages-equipements/equipements-pneumatique/'>Equipements Pneumatique</a>
                                                         </li></ul></li><li class='nav-item dropdown'>
                                                      <a class='dropdown-item dropdown-toggle' data-toggle='dropdown' href='javascript:void(0)'><span onclick='window.location="categories/outillage-a-main/"'>Outillage à main</span></a><ul class="dropdown-menu dropdown-submenu"><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillage-a-main/outillage-industriel/'>Outillage industriel</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillage-a-main/outillage-atelier/'>Outillage atelier</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillage-a-main/pack-fin-d-annee/'>Pack fin d'année</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outillage-a-main/special-automobile/'>Spécial automobile</a>
                                                         </li></ul></li><li class='nav-item dropdown'>
                                                      <a class='dropdown-item dropdown-toggle' data-toggle='dropdown' href='javascript:void(0)'><span onclick='window.location="categories/manutention-levage/"'>Manutention & levage</span></a><ul class="dropdown-menu dropdown-submenu"><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/manutention-levage/manutention/'>Manutention</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/manutention-levage/levage/'>Levage</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/manutention-levage/echafaudage-echelle-et-ecabeau/'>Echafaudage Echelle et Ecabeau</a>
                                                         </li></ul></li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/equipement-de-securite/'>Equipement de sécurité</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/materiel-thermique/'>Matériel Thermique</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/boulonnerie-visserie/'>Boulonnerie & Visserie</a>
                                                         </li><li class='nav-item dropdown'>
                                                      <a class='dropdown-item dropdown-toggle' data-toggle='dropdown' href='javascript:void(0)'><span onclick='window.location="categories/produit-siderurgique/"'>Produit sidérurgique</span></a><ul class="dropdown-menu dropdown-submenu"><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/produit-siderurgique/panneaux-sandwich/'>Panneaux sandwich</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/produit-siderurgique/tole/'>Tôle</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/produit-siderurgique/fer-marchand/'>Fer marchand</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/produit-siderurgique/aluminium-inox/'>Aluminium & inox</a>
                                                         </li></ul></li><li class='nav-item dropdown'>
                                                      <a class='dropdown-item dropdown-toggle' data-toggle='dropdown' href='javascript:void(0)'><span onclick='window.location="categories/soudage-plastique/"'>Soudage plastique</span></a><ul class="dropdown-menu dropdown-submenu"><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudage-plastique/soudage-bache/'>Soudage bâche</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudage-plastique/geomembranes-pehd-peld-pvc/'>Géomembranes (PEHD,PELD,PVC...)</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudage-plastique/etancheite-tpo-fpo/'>Étanchéité (TPO,FPO...)</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudage-plastique/revetements-de-sol/'>Revêtements de sol</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudage-plastique/accessoires-consommables/'>Accessoires & consommables</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/soudage-plastique/outils-a-main/'>Outils à main</a>
                                                         </li></ul></li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/cloture-et-grillage/'>Clôture et grillage</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/nouvel-arrivage/'>NOUVEL ARRIVAGE</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/outlet/'>Outlet</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/plaque-plastique/'>Plaque Plastique</a>
                                                         </li><li class='nav-item'>
                                                             <a class='dropdown-item' href='categories/eclairage/'>Eclairage</a>
                                                         </li></ul>						</li>
						   
                        						   <li class="nav-item "  style="background-color:#f50c0c">
							<a class="nav-link "  style="color:#e8e8ed  ;animation: mymove19 3s infinite;"  href="javascript:void(0)" >
							    <span onclick="window.location='https://www.samfi.tn/fr/a-decouvrir/nouvel-arrivage-telwin/'">Telwin							    							    </a>
                               						</li>
												<style>
						@keyframes mymove19{from{background-color:#f50c0c;color:#e8e8ed}to{background-color:#e8e8ed;color:#f50c0c}}
						</style>
                           
                        						   <li class="nav-item "  style="background-color:#faf0f0">
							<a class="nav-link "  style="color:#1212eb "  href="javascript:void(0)" >
							    <span onclick="window.location='https://www.samfi.tn/fr/categories/outillage-a-main/special-automobile/'">Spécial Automobile							    							    </a>
                               						</li>
												<style>
						@keyframes mymove41{from{background-color:#faf0f0;color:#1212eb}to{background-color:#1212eb;color:#faf0f0}}
						</style>
                           
                        						   <li class="nav-item " >
							<a class="nav-link "  href="javascript:void(0)" >
							    <span onclick="window.location='Nos-Partenaires/'">Nos Partenaires							    							    </a>
                               						</li>
						   
                        						   <li class="nav-item " >
							<a class="nav-link "  href="javascript:void(0)" >
							    <span onclick="window.location='catalogue-decembre/'">Catalogue							    							    </a>
                               						</li>
						   
                        						   <li class="nav-item "  style="background-color:#40ff00">
							<a class="nav-link "  style="color:#0a0106  ;animation: mymove42 3s infinite;"  href="javascript:void(0)" >
							    <span onclick="window.location='https://www.samfi.tn/fr/a-decouvrir/promos-ramadan/'">Promos Ramadan							    							    </a>
                               						</li>
												<style>
						@keyframes mymove42{from{background-color:#40ff00;color:#0a0106}to{background-color:#0a0106;color:#40ff00}}
						</style>
                           
                           
					</ul>
				</div>
			</div>			
			<a href="https://www.samfi.tn/fr/compte/" class="acces-client"> <img src="../dist/images/login_circle.png" class="img-fluid me-2">Accès client  </a>
		</div>
	</nav>
	<!---------------- Fin Nav-bar ------------------>
	
		<div class="d-block d-lg-none text-center mt-3 mb-1">
			<a class="btn mb-2" style="color:#fcfcfc  ;background-color:#cf780f;animation: mymove-1 3s infinite;font-weight: 600;" href="https://www.samfi.tn/fr/a-decouvrir/promos-ramadan/" >
		Les Meilleures affaires du Ramadan chez SAMFI		</a>
		<style>
		@keyframes mymove-1{to{background-color:#cf780f;color:#fcfcfc}from{background-color:#fcfcfc;color:#cf780f}}
		</style>
			<a class="btn mb-2" style="color:#f0f0f0  ;background-color:#eb1515;animation: mymove-4 3s infinite;font-weight: 600;" href="https://www.samfi.tn/fr/a-decouvrir/nouvel-arrivage-telwin/" >
		Nouvel arrivage de la marque Italienne TELWIN		</a>
		<style>
		@keyframes mymove-4{to{background-color:#eb1515;color:#f0f0f0}from{background-color:#f0f0f0;color:#eb1515}}
		</style>
			<a class="btn mb-2" style="color:#e1ff00  ;background-color:#1a0404;animation: mymove-5 3s infinite;font-weight: 600;" href="https://www.samfi.tn/fr/recherche/?search=grillage+rigide&action=search" >
		Panneau de Grillage CLR : La clôture qui dure !		</a>
		<style>
		@keyframes mymove-5{to{background-color:#1a0404;color:#e1ff00}from{background-color:#e1ff00;color:#1a0404}}
		</style>
		</div>
		
		
	      
        
		<section class="selection-breadcrumbs">
			<div class="container container-custom">
	<!---------------- Breadcrumb ----------------------->


                <div class="breadcrumbs my-3">	
                    <ol class="justify-content-start">
                        <li><i class="fa fa-home"></i> <a href="https://www.samfi.tn/fr/">Accueil</a></li>
                        <li><a href="categories/ ">Catalogue</a></li>            			<li><a href="categories/produit-siderurgique/ ">Produit sidérurgique</a></li>            			<li>fer marchand</li>            			            			            			                    </ol>
                </div>	
	<!--------------- Fin Breadcrumb ----------------->
			</div>
		</section>
      
		<section class="selection mb-3" id="section-selection">
			<div class="container container-custom">
				<div class="section-selection position-relative" style="min-height:230px">
					<a href="https://www.samfi.tn/fr/categories/produit-siderurgique/fer-marchand/" class="bloc-selection text-center d-block" style="background:url('../media/products/50-categ-entete-ferr.jpg') no-repeat center center;background-size: cover;height: 100%;min-height:230px">
					    
        				        					<div class="title position-absolute top-0 end-0 mt-4 me-4 text-end">
        						<h2 class="mt-2 mb-0"> Produit sidérurgique <span style="color: #f45000;font-weight: 700;">/</span></h2>
        						            					<h3 class="mt-2 mb-0">Fer marchand </h3>
            				    								        					</div>
        				                        					</a>
				</div>
			</div>
		</section>
	


	
	<div class="main">
	
	
	
	
	
	<section class="bloc_accueil my-3">
        
        <div class="container container-custom">
        
            <div class="row">
        		
        		

    <div class="col-md-3 left-content mb-4 order-2 order-md-1">
        
        		<div class="shop_sidebar_area bg-white rounded">
    		<div class="filter mb-3">
    			<h3> Filter</h3>
    		</div>
            
            <div class="shop_sidebar_area_section">
    			
                <form action="recherche/" method="get" enctype="multipart/form-data">
                <!-- ##### Single Widget ##### -->
                <div class="widget brands">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4">Catégories</h3>
					                    <!--  Catagories  -->
                    <div class="widget-desc">
                        
                            <ul class="list-unstyled m-0">
                                                	        	                    
        	                    <div class="form-check category px-4">
                                    <input class="form-check-input common_selector category_selector d-none" type="checkbox" name="categories[]" value="48" id="panneaux-sandwich"  >
                                    <label class="form-check-label" for="panneaux-sandwich">Panneaux sandwich </label><i class="fa fa-angle-right ms-1"></i>
                                </div>

    	                                       	        	                    
        	                    <div class="form-check category px-4">
                                    <input class="form-check-input common_selector category_selector d-none" type="checkbox" name="categories[]" value="49" id="tole"  >
                                    <label class="form-check-label" for="tole">Tôle </label><i class="fa fa-angle-right ms-1"></i>
                                </div>

    	                                       	        	                    
        	                    <div class="form-check category px-4">
                                    <input class="form-check-input common_selector category_selector d-none" type="checkbox" name="categories[]" value="50" id="fer-marchand"  >
                                    <label class="form-check-label" for="fer-marchand">Fer marchand </label><i class="fa fa-angle-right ms-1"></i>
                                </div>

    	                                       	        	                    
        	                    <div class="form-check category px-4">
                                    <input class="form-check-input common_selector category_selector d-none" type="checkbox" name="categories[]" value="52" id="aluminium-inox"  >
                                    <label class="form-check-label" for="aluminium-inox">Aluminium & inox </label><i class="fa fa-angle-right ms-1"></i>
                                </div>

    	                       	                   </ul>
                    </div>
                </div>
    
                <!-- ##### Single Widget ##### -->
                <div class="widget brands ">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4">Marques</h3>
    
                    <div class="widget-desc">
                            					
                        <!-- Single Form Check -->
                        <div class="form-check px-4">
                            <input class="form-check-input common_selector marque_selector ms-auto" type="checkbox" name="marques[]" value="29" id="Sans Nom" >
                            <label class="form-check-label ms-2" for="Sans Nom">Sans Nom</label>
                        </div>
    					    					
                        <!-- Single Form Check -->
                        <div class="form-check px-4">
                            <input class="form-check-input common_selector marque_selector ms-auto" type="checkbox" name="marques[]" value="38" id="." >
                            <label class="form-check-label ms-2" for=".">.</label>
                        </div>
    					    					
                        <!-- Single Form Check -->
                        <div class="form-check px-4">
                            <input class="form-check-input common_selector marque_selector ms-auto" type="checkbox" name="marques[]" value="42" id="CLR" >
                            <label class="form-check-label ms-2" for="CLR">CLR</label>
                        </div>
    					                        
                    </div>
                </div>
                <!-- ##### Single Widget ##### -->
                <div class="widget brands ">
                    <!-- Widget Title -->
                    <h3 class="widget-title px-4">Stock</h3>
    
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
                    <h3 class="widget-title px-4">Prix</h3>
    
                    <div class="widget-desc">
                        <div class="slider-range px-4">
                            	
														<label class="my-1">Min (DT)</label>
        					<input type="text" id="hidden_minimum_price" name="minimum_price" class="form-control" value="0.000" />
                            <label class="my-1">Max (DT)</label>
                            <input type="text" id="hidden_maximum_price" name="maximum_price" class="form-control" value="125356.244" />
                            
						</div>
                    </div>
                    <button type="submit" class="btn btn-search mx-4 mt-3">Rechercher</button>
					<input type="hidden" name="action" value="search">
										<input type="hidden" name="categorie" value="34">
					                </div>
                
                </form>
                
            </div>
        
        </div>				        
								
			
					
	<div class="service-content bg-white rounded mt-3">
					       
		            <div class="d-flex align-items-center p-3 border-section">
                <img src="../media/services/1-service-livraison.png" class="img-fluid"/>
                <div class="ms-3 w-100">
                    <h4>Livraison à  domicile assurée</h4>
                    <p><p><font style="vertical-align:inherit"><font style="vertical-align:inherit">Livraison entre 24 et 72 heures</font></font></p></p>
                </div>
            </div>
                    <div class="d-flex align-items-center p-3 border-section">
                <img src="../media/services/2-service-retour.png" class="img-fluid"/>
                <div class="ms-3 w-100">
                    <h4>Garantie offerte</h4>
                    <p><p>Notez que la garantie du fabricant suit toujours nos produits</p></p>
                </div>
            </div>
                    <div class="d-flex align-items-center p-3 border-section">
                <img src="../media/services/3-service-paiement.png" class="img-fluid"/>
                <div class="ms-3 w-100">
                    <h4>Consultez-nous</h4>
                    <p><p>Commercial.digital@samfi.tn</p>

<p><a href="mailto:Offre@samfi.tn">Offre@samfi.tn</a>&nbsp;</p></p>
                </div>
            </div>
                    <div class="d-flex align-items-center p-3 border-section">
                <img src="../media/services/4-service-service-client.png" class="img-fluid"/>
                <div class="ms-3 w-100">
                    <h4>Service clients en Ligne</h4>
                    <p><p>☎️ <a href="tel:58 581 318">58 581 318</a>&nbsp;</p>

<p><span style="background-color:#ffffff; color:#000000">☎️ </span><a href="tel:58 581 318">58 581 312</a>&nbsp;</p>

<p>☎️ <a href="tel:58 581 318">58 581 327</a></p></p>
                </div>
            </div>
                    <div class="d-flex align-items-center p-3 border-section">
                <img src="../media/services/5-Service-images-removebg-preview.jpg" class="img-fluid"/>
                <div class="ms-3 w-100">
                    <h4>Questions sur votre commande ?</h4>
                    <p><p>Contactez nous au&nbsp;<a href="https://wa.me/58581312"><span style="color:#e67e22"><strong>58 58 13 12</strong></span></a></p></p>
                </div>
            </div>
        	
	</div>    </div>        		
        		
        		
        		<div class="col-md-9 right-content order-1 order-md-2">
        		                    		
        		    
                				
			<div class="produits  custom-slick-box">
				<div class="mt-3">
    				<h2>Produits : Fer marchand</h2>
    				<div class="divider"></div>
				</div>
				
				<div class="prod-content border-0">
				                
				                      
                                        											<div class=" row  "> 
																						<div class="col-md-12 row align-items-center sort-section justify-content-end mx-0 py-2">
												<div class="col-md-6 text-end">
													<select name="ordre" class="show-tick form-control sort" onchange="window.location=this.value;">
													   <option value="0">Trier par</option>
													   <option value="categories/produit-siderurgique/fer-marchand/sort/PRIX_ASC/">Du moins cher au plus cher</option>
													   <option value="categories/produit-siderurgique/fer-marchand/sort/PRIX_DESC/">Du plus cher au moins cher</option>
													   <option value="categories/produit-siderurgique/fer-marchand/sort/ALPHA_ASC/">Ordre alphabétique Croissant</option>
													   <option value="categories/produit-siderurgique/fer-marchand/sort/ALPHA_DESC/">Ordre alphabétique Décroissant</option>
													</select>
												</div>  
											</div> 
																						
<div class="col-md-12 col-xs-12 ">
			             <nav aria-label="Page navigation example">
                            <ul class="pagination"><li class="page-item active" aria-current="page"><a class="page-link" href="#">1</a></li><li class="page-item" aria-current="page"><a href="categories/produit-siderurgique/fer-marchand/2/"  class="page-link">2</a></li>      </ul>
                        </nav>
                    </div>            			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/tube-rond-acier/" class="d-block h-100 w-100"><img src="../media/products/3990-produits-tube-ron1d.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/tube-rond-acier/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3990">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3990"  onclick="addToWishList('3990');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/tube-rond-acier/" class="">
                    											<h3>Tube Rond Acier</h3>
                    										</a>
                    										                        									<p class="product-price m-0">191.944 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">213.271 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3990") != null){
                                                            document.getElementById("clock3990").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3990") != null){
                                                                document.getElementById("clock3990").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/tube-rectangulaire-acier/" class="d-block h-100 w-100"><img src="../media/products/3989-produits-Tubes-rectangles-galvanisee.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/tube-rectangulaire-acier/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3989">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3989"  onclick="addToWishList('3989');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/tube-rectangulaire-acier/" class="">
                    											<h3>Tube Rectangulaire Acier</h3>
                    										</a>
                    										                        									<p class="product-price m-0">76.400 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">89.882 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3989") != null){
                                                            document.getElementById("clock3989").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3989") != null){
                                                                document.getElementById("clock3989").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/tube-rampe-escalier/" class="d-block h-100 w-100"><img src="../media/products/3988-produits-tube-rampe-esaclier.JPG.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/tube-rampe-escalier/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3988">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3988"  onclick="addToWishList('3988');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/tube-rampe-escalier/" class="">
                    											<h3>Tube Rampe Escalier</h3>
                    										</a>
                    										                        									<p class="product-price m-0">23.751 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">26.390 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3988") != null){
                                                            document.getElementById("clock3988").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3988") != null){
                                                                document.getElementById("clock3988").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-lightgreen avaibility p-2" style="font-weight:400;font-size:12px"> En stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/tube-carre-en-acier/" class="d-block h-100 w-100"><img src="../media/products/3987-produits-tube-carre-laminee-a-froid.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/tube-carre-en-acier/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3987">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3987"  onclick="addToWishList('3987');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/tube-carre-en-acier/" class="">
                    											<h3>Tube Carré  En Acier</h3>
                    										</a>
                    										                        									<p class="product-price m-0">17.699 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">19.666 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3987") != null){
                                                            document.getElementById("clock3987").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3987") != null){
                                                                document.getElementById("clock3987").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-lightgreen avaibility p-2" style="font-weight:400;font-size:12px"> En stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/lame-ressort/" class="d-block h-100 w-100"><img src="../media/products/3979-produits-ressort-a-lame-.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/lame-ressort/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3979">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3979"  onclick="addToWishList('3979');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/lame-ressort/" class="">
                    											<h3>Lame Ressort</h3>
                    										</a>
                    										                        									<p class="product-price m-0">8.375 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">9.306 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3979") != null){
                                                            document.getElementById("clock3979").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3979") != null){
                                                                document.getElementById("clock3979").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-upn/" class="d-block h-100 w-100"><img src="../media/products/3978-produits-Poutrelles-fer-upn.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-upn/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3978">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3978"  onclick="addToWishList('3978');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-upn/" class="">
                    											<h3>Fer En Forme De Upn</h3>
                    										</a>
                    										                        									<p class="product-price m-0">295.782 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">328.647 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3978") != null){
                                                            document.getElementById("clock3978").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3978") != null){
                                                                document.getElementById("clock3978").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-u/" class="d-block h-100 w-100"><img src="../media/products/3977-produits-fer-u.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-u/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3977">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3977"  onclick="addToWishList('3977');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-u/" class="">
                    											<h3>Fer En Forme De U</h3>
                    										</a>
                    										                        									<p class="product-price m-0">29.988 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">33.320 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3977") != null){
                                                            document.getElementById("clock3977").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3977") != null){
                                                                document.getElementById("clock3977").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-t/" class="d-block h-100 w-100"><img src="../media/products/3976-produits-fer-T.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-t/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3976">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3976"  onclick="addToWishList('3976');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-de-t/" class="">
                    											<h3>Fer En Forme De T</h3>
                    										</a>
                    										                        									<p class="product-price m-0">36.088 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">40.098 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3976") != null){
                                                            document.getElementById("clock3976").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3976") != null){
                                                                document.getElementById("clock3976").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/fer-rond/" class="d-block h-100 w-100"><img src="../media/products/3975-produits-fer-rond.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/fer-rond/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3975">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3975"  onclick="addToWishList('3975');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
                            	                                    </button>
                                                                </div>
                                                                                    									    </div>    
                    									        
                    									</div>
                    								</div>
                    
                    									<!-- Product Meta Data -->
                    									<div class="product-meta-data">
                        									<!-- Ratings & Cart -->
                        									<div class="ratings-cart d-flex align-items-center justify-content-center">
                        									  	<div class="rating2" data-rateyo-rating="0.0000" data-rateyo-num-stars="5"  data-rateyo-score="0.0000"> </div>
															</div>
                    										<a href="produit/produit-siderurgique/fer-marchand/fer-rond/" class="">
                    											<h3>Fer Rond</h3>
                    										</a>
                    										                        									<p class="product-price m-0">834.488 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">927.209 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3975") != null){
                                                            document.getElementById("clock3975").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3975") != null){
                                                                document.getElementById("clock3975").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/fer-plat/" class="d-block h-100 w-100"><img src="../media/products/3974-produits-fer-plat.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/fer-plat/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3974">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3974"  onclick="addToWishList('3974');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/fer-plat/" class="">
                    											<h3>Fer Plat</h3>
                    										</a>
                    										                        									<p class="product-price m-0">220.578 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">245.086 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3974") != null){
                                                            document.getElementById("clock3974").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3974") != null){
                                                                document.getElementById("clock3974").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-ipe/" class="d-block h-100 w-100"><img src="../media/products/3973-produits-pourtrelles-fer-ipe.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-ipe/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3973">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3973"  onclick="addToWishList('3973');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-ipe/" class="">
                    											<h3>Fer En Forme  Ipe</h3>
                    										</a>
                    										                        									<p class="product-price m-0">2.830 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">3.144 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3973") != null){
                                                            document.getElementById("clock3973").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3973") != null){
                                                                document.getElementById("clock3973").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                                			                    <div class=" col-md-4 mt-2  mb-3">
                    							<div class="card p-2 cursor-pointer border-0 h-100 position-relative">
                    							    
													<!-- Avaiable -->
													<div class="position-absolute start-0 top-0 ms-2 mt-2" style="z-index:2">																
														<p class="bg-danger avaibility text-white p-2"> Hors stock</p>														
																											</div>
                    								<!-- Product Image -->
                    								<div class="product-img position-relative">
                    									<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-heb/" class="d-block h-100 w-100"><img src="../media/products/3972-produits-FER-HEB.webp" alt="" class="img-fluid"></a>
                    									<div class="hover-zoom position-absolute w-100 h-100 start-0 top-0">
                    									    
                    									   <div class="d-flex position-absolute start-50 top-50 translate-middle ">
                        									    <a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-heb/" class="d-block cart-icone-blue">
                        									        <i class="fa fa-eye"></i>
                        									    </a>
                        									                                
                                                                
                                                                <div class="wishlist" id="wishlist3972">
                            	                                    <button type="button" class="d-block cart-icone-blue " id="btn-wishlist3972"  onclick="addToWishList('3972');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris" >
                            	                                        <i class="fa fa-heart-o" aria-hidden="true"></i>
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
                    										<a href="produit/produit-siderurgique/fer-marchand/fer-en-forme-heb/" class="">
                    											<h3>Fer En Forme  Heb</h3>
                    										</a>
                    										                        									<p class="product-price m-0">0.000 DT  <span style="text-decoration:line-through;color:#aaa;font-size: 14px;">0.000 DT</span> </p>
                        									                    									</div>
                    							</div>
                    							
                    						
                    						
                                    		    <script>
                                                                                                        var countDownDate = new Date("January 01, 1970 ").getTime();
                                                    // Update the count down every 1 second
                                                    var x = setInterval(function() {
                                                        var now = new Date().getTime();
                                                        // Find the distance between now an the count down date
                                                        var distance = countDownDate - now;
                                                        // Time calculations for days, hours, minutes and seconds
                                                        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                                                        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                                                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                                                        if (distance < 0) {
                                                            clearInterval(x);
                                                            if(document.getElementById("clock3972") != null){
                                                            document.getElementById("clock3972").innerHTML = "Clôturé";
															}
                                                        }else{
                                                            if(document.getElementById("clock3972") != null){
                                                                document.getElementById("clock3972").innerHTML = days + "J : " + hours + "H : " +  minutes + "MN " ;
                                                            }
                                                        }
                                                    }, 1000);
                                                </script>
                    						</div>
                                    		
                		                    											</div>
											<div class="col-md-12 col-xs-12 ">
			             <nav aria-label="Page navigation example">
                            <ul class="pagination"><li class="page-item active" aria-current="page"><a class="page-link" href="#">1</a></li><li class="page-item" aria-current="page"><a href="categories/produit-siderurgique/fer-marchand/2/"  class="page-link">2</a></li>      </ul>
                        </nav>
                    </div>                		          
    		          </div>
				
				
			</div>
							
				
				        		
        		</div>
            	
        		

    <div class="col-md-12 full-content order-3">
				
				<div class="call-to-action">				        
                		        
			            <div class="cat-bloc mb-4" style="background:url('../media/site/15-bloc-devis-samfi-rapide.png') no-repeat center center;background-size:cover;position: relative;height: 200px;">
			                <a href="demande-devis/" class="btn btn-devis"><i class="fa fa-file me-2 rounded-50"></i> Demandez un devis</a>        						    
        				</div>
				</div>
                    </div>						    
		    </div>
		    
		</div>
		
	</section>	
	

	<footer class="footer pt-4">
		<div class="container container-custom">

			<div class="row border-bottom">
				<div class="col-lg-3 col-md-6 mb-4 infos">
				    <h3>INFORMATIONS</h3>
				    <ul class="list-unstyled">
				        <li> <i class="fa fa-angle-double-right me-1"></i><a href="la-societe/">La société</a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="Livraison-domicile/Livraison-domicile/">Livraison à domicile</a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="conditions-generales-de-vente/">Conditions Générales de Vente</a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="Commandez-chez-SAMFI/">Commandez chez SAMFI</a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="nos-points-de-vente/">Nos points de vente</a></li>
				    </ul>
				</div>
				<div class="col-lg-3 col-md-6 mb-4 infos">
				    <h3>NOTRE CATALOGUE</h3>
				    <ul class="list-unstyled">
				        				        <li> <i class="fa fa-angle-double-right me-1"></i><a href="categories/soudure-accessoires/"> Soudure & accessoires   </a></li>
				        				        <li> <i class="fa fa-angle-double-right me-1"></i><a href="categories/outillages-equipements/"> Outillages & équipements   </a></li>
				        				        <li> <i class="fa fa-angle-double-right me-1"></i><a href="categories/outillage-a-main/"> Outillage à main   </a></li>
				        				        <li> <i class="fa fa-angle-double-right me-1"></i><a href="categories/manutention-levage/"> Manutention & levage   </a></li>
				        				        <li> <i class="fa fa-angle-double-right me-1"></i><a href="categories/equipement-de-securite/"> Equipement de sécurité   </a></li>
				        				    </ul>
				</div>
				<div class="col-lg-3 col-md-6 mb-4 infos">
				    <h3>ESPACE CLIENT</h3>
				    <ul class="list-unstyled">
				        <li> <i class="fa fa-angle-double-right me-1"></i><a href="https://wa.me/58581312"> Commander au 58581312</a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="https://www.samfi.tn/fr/compte/"> Mon compte  </a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="compte/mes-commandes/"> Historique des commandes </a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="conditions-retour/">Conditions de retour</a></li>
                        <li> <i class="fa fa-angle-double-right me-1"></i><a href="garantie-service-apres-vente-sav/">Garantie & Service Après-Vente (SAV)</a></li>
				    </ul>
				</div>
				<div class="col-lg-3 col-md-6 mb-4 newsletter">
					<h3>Inscrivez-vous à la
                    <span>Newsletter</span></h3>
                    <p>Abonnez-vous à notre lettre d'informations
                    et reste informés des nouveautés SAMFI</p>
					<form  action="" method="post" id="contact-forms"  role="form" name="newsletter" onsubmit="return get_value1();">
						<input class="form-control newsletter-email" type="email" required  name="mail" id="email" placeholder="Votre adresse e-mail...">
						<button type="submit" class="btn btn-abonn">S'abonner</button>
					</form>
					<div class="reseaux-sociaux mt-3">
    					<div class="reseaux-sociaux-icones">
					    <span>Nous suivre</span>
    			  	        				    <a href="https://fr-fr.facebook.com/SAMFI.TUNISIE/"  target="_blank"><i class="fa fa-facebook"></i> </a>
    				        				    <a href="https://www.instagram.com/samfi_tunisie/"  target="_blank"><i class="fa fa-instagram"></i> </a>
    				        				    <a href="https://tn.linkedin.com/company/samfitn"  target="_blank"><i class="fa fa-linkedin"></i> </a>
    				        				    <a href="https://wa.me/58581324"  target="_blank"><i class="fa fa-whatsapp"></i> </a>
    				        				    <a href="https://www.youtube.com/@Samfi-Tunisie"  target="_blank"><i class="fa fa-youtube-play"></i> </a>
    				    				
    					</div>
					</div>
				</div>
			</div>
			<div class="pied-page text-center">
				<p>	
					Copyright © 2023 SAMFI - Tous droits réservés.				</p>
			</div>
			
		</div>		
	</footer>
		<div class="wabtn" id="wabutton">
  <style> [wa-tooltip] { position: relative; cursor: default;  &:hover { &::before { content: attr(wa-tooltip); font-size: 16px; text-align: center; position: absolute; display: block; right: calc(0% - 100px); left: null; min-width: 200px; max-width: 200px; bottom: calc(100% + 10px); transform: translate(-50%); animation: fade-in 500ms ease; background: #00E785; border-radius: 4px; padding: 10px; color: #ffffff; z-index: 1; } } }  @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }  [wa-tooltip] {  }  @keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }</style>
  <a wa-tooltip="Nous sommes disponible! Clique ici pour discuter" target="_blank" href="https://wa.me/+21658581318?text=" style=" cursor: pointer;height: 62px;width: auto;padding: 10px 10px 10px 10px;position: fixed !important;color: #fff;bottom: 20px;right: 20px;;display: flex;font-size: 18px;font-weight: 600;align-items: center;z-index: 999999999 !important;background-color: #00E785;box-shadow: 4px 5px 10px rgba(0, 0, 0, 0.4);border-radius: 100px;animation: pulse 2.5s ease infinite;">
    <svg width="42" height="42" style="padding: 5px;" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_1024_354)"><path d="M23.8759 4.06939C21.4959 1.68839 18.3316 0.253548 14.9723 0.0320463C11.613 -0.189455 8.28774 0.817483 5.61565 2.86535C2.94357 4.91323 1.10682 7.86244 0.447451 11.1638C-0.21192 14.4652 0.351026 17.8937 2.03146 20.8109L0.0625 28.0004L7.42006 26.0712C9.45505 27.1794 11.7353 27.7601 14.0524 27.7602H14.0583C16.8029 27.7599 19.4859 26.946 21.768 25.4212C24.0502 23.8965 25.829 21.7294 26.8798 19.1939C27.9305 16.6583 28.206 13.8682 27.6713 11.1761C27.1367 8.48406 25.8159 6.01095 23.8759 4.06939ZM14.0583 25.4169H14.0538C11.988 25.417 9.96008 24.8617 8.1825 23.8091L7.7611 23.5593L3.3945 24.704L4.56014 20.448L4.28546 20.0117C2.92594 17.8454 2.32491 15.2886 2.57684 12.7434C2.82877 10.1982 3.91938 7.80894 5.67722 5.95113C7.43506 4.09332 9.76045 2.87235 12.2878 2.48017C14.8152 2.08799 17.4013 2.54684 19.6395 3.78457C21.8776 5.02231 23.641 6.96875 24.6524 9.3179C25.6638 11.6671 25.8659 14.2857 25.2268 16.7622C24.5877 19.2387 23.1438 21.4326 21.122 22.999C19.1001 24.5655 16.6151 25.4156 14.0575 25.4157L14.0583 25.4169Z" fill="#E0E0E0"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6291 7.98363C10.3723 7.41271 10.1019 7.40123 9.85771 7.39143C9.65779 7.38275 9.42903 7.38331 9.20083 7.38331C9.0271 7.3879 8.8562 7.42837 8.69887 7.5022C8.54154 7.57602 8.40119 7.68159 8.28663 7.81227C7.899 8.17929 7.59209 8.62305 7.38547 9.11526C7.17884 9.60747 7.07704 10.1373 7.08655 10.6711C7.08655 12.3578 8.31519 13.9877 8.48655 14.2164C8.65791 14.4452 10.8581 18.0169 14.3425 19.3908C17.2382 20.5327 17.8276 20.3056 18.4562 20.2485C19.0848 20.1913 20.4843 19.4194 20.7701 18.6189C21.056 17.8183 21.0557 17.1323 20.9701 16.989C20.8844 16.8456 20.6559 16.7605 20.3129 16.5889C19.9699 16.4172 18.2849 15.5879 17.9704 15.4736C17.656 15.3594 17.4275 15.3023 17.199 15.6455C16.9705 15.9888 16.3139 16.7602 16.1137 16.9895C15.9135 17.2189 15.7136 17.2471 15.3709 17.0758C14.3603 16.6729 13.4275 16.0972 12.6143 15.3745C11.8648 14.6818 11.2221 13.8819 10.7072 13.0007C10.5073 12.6579 10.6857 12.472 10.8579 12.3007C11.0119 12.1472 11.2006 11.9005 11.3722 11.7003C11.5129 11.5271 11.6282 11.3346 11.7147 11.1289C11.7603 11.0343 11.7817 10.9299 11.7768 10.825C11.7719 10.7201 11.7409 10.6182 11.6867 10.5283C11.6001 10.3566 10.9337 8.66151 10.6291 7.98363Z" fill="white"></path><path d="M23.7628 4.02445C21.4107 1.66917 18.2825 0.249336 14.9611 0.0294866C11.6397 -0.190363 8.35161 0.804769 5.70953 2.82947C3.06745 4.85417 1.25154 7.77034 0.600156 11.0346C-0.051233 14.299 0.506321 17.6888 2.16894 20.5724L0.222656 27.6808L7.49566 25.7737C9.50727 26.8692 11.7613 27.4432 14.0519 27.4434H14.0577C16.7711 27.4436 19.4235 26.6392 21.6798 25.1321C23.936 23.6249 25.6947 21.4825 26.7335 18.9759C27.7722 16.4693 28.0444 13.711 27.5157 11.0497C26.9869 8.38835 25.6809 5.94358 23.7628 4.02445ZM14.0577 25.1269H14.0547C12.0125 25.1271 10.0078 24.5782 8.25054 23.5377L7.8339 23.2907L3.51686 24.4222L4.66906 20.2143L4.39774 19.7831C3.05387 17.6415 2.4598 15.1141 2.70892 12.598C2.95804 10.082 4.03622 7.72013 5.77398 5.88366C7.51173 4.04719 9.81051 2.84028 12.3089 2.45266C14.8074 2.06505 17.3638 2.5187 19.5763 3.74232C21.7888 4.96593 23.5319 6.89011 24.5317 9.21238C25.5314 11.5346 25.7311 14.1233 25.0993 16.5714C24.4675 19.0195 23.0401 21.1883 21.0414 22.7367C19.0427 24.2851 16.5861 25.1254 14.0577 25.1255V25.1269Z" fill="white"></path></g><defs><clipPath id="clip0_1024_354"><rect width="27.8748" height="28" fill="white" transform="translate(0.0625)"></rect></clipPath></defs></svg>
    <span class="button-text"></span>
  </a>
</div>
	
	</div>

	
    
    
    <script type="text/javascript">
        function addToWishList(idproduit) {
              var favoris = "";
              var idclient = "";
              var wishList = document.getElementById('wishlist'+idproduit);
              var btnWishList = document.getElementById('btn-wishlist'+idproduit);
              var blocWishList = document.getElementById('blocWishList');
              
              $.ajax({
                url: "includes/addwishlist.php",
                type: "GET",
			    data: 'idproduit=' + idproduit + '&idclient=' + idclient ,
		        dataType: "json",
                success: function(data) {
                    btnWishList.innerHTML = '<i class="fa fa-heart" aria-hidden="true"></i>';
                    document.getElementById('blocWishList').innerHTML = data[0];
    
                    $(wishList).html('<button type="button" class="d-block cart-icone-blue" id="btn-wishlist'+idproduit+'" onclick="removeFromWishList('+idproduit+');"  ><i class="fa fa-heart" aria-hidden="true"></i></button>');
    
                    //window.location.reload()
                }
              })
        }
        function removeFromWishList(idproduit) {
              var favoris = "";
              var idclient = "";
              var wishList = document.getElementById('wishlist'+idproduit);
              var btnWishList = document.getElementById('btn-wishlist'+idproduit);
              var blocWishList = document.getElementById('blocWishList');
              
              $.ajax({
                url: "includes/removewishlist.php",
                type: "GET",
			    data: 'idproduit=' + idproduit + '&idclient=' + idclient ,
		        dataType: "json",
                success: function(data) {
                    
                    btnWishList.innerHTML = '<i class="fa fa-heart-o" aria-hidden="true"></i>';
                    document.getElementById('blocWishList').innerHTML = data[0];
    
                    $(wishList).html('<button type="button" class="d-block cart-icone-blue" id="btn-wishlist'+idproduit+'" onclick="addToWishList('+idproduit+');"  data-bs-toggle="tooltip" data-bs-placement="right" title="Ajouter au favoris"><i class="fa fa-heart-o" aria-hidden="true"></i></button>');
    
                    //window.location.reload()
                }
              })
        }
    </script>
       
  	
  
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
  
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    
	
    <script src="../assets/vendor/aos/aos.js"></script>
    
    <script src="../assets/vendor/php-email-form/validate.js"></script>
    
    <!-- All js plugins included in this file. -->
    <script src="../dist/js/plugins.js"></script>
    
    <!-- Main js file that contents all jQuery plugins activation. -->
    <script src="../dist/js/main.js"></script>
	
	<!-- Typehead Plugin JavaScript -->
    <script src="../dist/js/typeahead.js"></script>
    
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

  	<script src="../dist/js/slick.js"></script>  
	
	<script type="text/javascript">
		$(document).ready(function(){
			$('.products-home-box').slick({
			    rows: 2,
				infinite: true,
				slidesPerRow: 4,
                arrows: true,
				autoplay: true,
				autoplaySpeed: 7500,
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
				slidesToShow: 9,
				slidesToScroll: 1,
				infinite: true,
				autoplay: true,
				autoplaySpeed: 7500,
				arrows: true,
				dots: false,
        		prevArrow: '<img src="../dist/images/left-arrow.png" class="img-fluid slick-prev slick-grey"><img src="../dist/images/left-arrow-orange.png" class="img-fluid slick-prev slick-orange">',
        		nextArrow: '<img src="../dist/images/right-arrow.png" class="img-fluid slick-next slick-grey"><img src="../dist/images/right-arrow-orange.png" class="img-fluid slick-next slick-orange">',
				pauseOnHover: false,
				responsive: [{
					breakpoint: 992,
					settings: {
						slidesToShow: 3
					}
				}, {
					breakpoint: 768,
					settings: {
						slidesToShow: 3
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
				infinite: true,
				autoplay: true,
				arrows: true,
				dots: false,
				autoplaySpeed: 7500,
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
				autoplay: true,
				dots: false,
				autoplaySpeed: 7500,
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
				autoplay: true,
				autoplaySpeed: 7500,
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
						slidesPerRow: 1
					}
				}]
			});
			$('a[data-bs-toggle="tab"]').on('shown.bs.tab', function(e) {
				$('.box-tablist').slick('setPosition');
			});
						
			$('.prod-sim-box').slick({
				slidesToShow: 3,
				slidesToScroll: 1,
				infinite: true,
				autoplay: true,
				autoplaySpeed: 7500,
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
                ratedFill: "#ff9b6d",
                starWidth: "20px",
                readOnly: true
            });
            $("#rating2").rateYo({
                normalFill: "#cbcbcb",
                ratedFill: "#ff9b6d",
                starWidth: "20px",
                readOnly: true
            });
            $("#rating").rateYo({
                starWidth: "20px",
                normalFill: "#cbcbcb",
                ratedFill: "#ff9b6d"
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

	<script src="../dist/js/zoomsl.js"></script>
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
                    function selectOptionValues(value){
                        
                        var idopt = value;
                        var qteop = document.getElementById('qty').value;
                        $.post('includes/price_values.php',{ idopt : idopt },
                            function(data){ 
                                document.getElementById('priceValue').innerHTML = data;
                                document.getElementById('qty').value='1';
                            }
                        );

                        $.post('includes/get_qty.php',{ idopt : idopt },
                            function(data){ 
                                document.getElementById('qtydispo').value=data;
                            }
                        );
                        
                        $.post('includes/qte_values.php',{ idopt : idopt,qteop:qteop },
                            function(data){ 
                                document.getElementById('stock').innerHTML = data;
                                validate(data && !data.includes("rupture") ? 1 : 0);
								if (data != "") {
									var com = data.includes("qtecom");
									var res = data.includes("qteres");
									var rup = data.includes("rupture");
									var qty = 'qty';
									var urlP = 'https://www.samfi.tn/fr/panier/';
									if (res){ 
										document.getElementById('priceValue').style.display="none";
										document.getElementById('idCheckout').innerHTML='<button type="button" class="btn w-100 text-uppercase px-3 py-2" data-bs-toggle="modal" data-bs-target="#preCommande" id="openModalCom"> <img src="../dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain"> Pré-commander</button>';
									}
									else{ 
										document.getElementById('priceValue').style.display="block";
										if (com){ 
											document.getElementById('idCheckout').innerHTML='<button type="button" class="btn w-100 text-uppercase px-3 py-2" data-bs-toggle="modal" data-bs-target="#preCommande"  id="openModalCom" > <img src="../dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain"> Pré-commander</button>';
										}else{ 
											if (rup){ 
												document.getElementById('idCheckout').innerHTML='<button type="submit" name="addtocart1" id="checkout" class="btn w-100 text-uppercase px-3 py-2" disabled="disabled"> <img src="../dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain"> Ajouter à mon panier</button>';
											}else{
												document.getElementById('idCheckout').innerHTML='<button type="submit" name="addtocart1" id="checkout" class="btn w-100 text-uppercase px-3 py-2" > <img src="../dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain"> Ajouter à mon panier</button>	<input type="text" name="action" value="add" hidden >';
												//<button type="button" name="addtocart" class="btn w-100 text-uppercase px-3 py-2"  onclick="addToCart(50, document.getElementById('+qty+').value); window.setTimeout(function () { location.href='+urlP+' },1000);"> <img src="../dist/images/shopping-cart.png" class="img-fluid" style="object-fit:contain"> Ajouter à mon panier</button>';	
											}
										}
									}
									var captchaWidget; // id du widget captcha

									function onLoadCaptcha() {
									  // Callback appelé quand api.js est chargée
									  console.log("API reCAPTCHA chargée");
									}

									$("#openModalCom").on("click", function() {
										// Quand le contenu est chargé, rendre le reCAPTCHA
										if (typeof grecaptcha !== "undefined") {
										  captchaWidget = grecaptcha.render("recaptcha-container", {
											"sitekey": "6LdbVVIpAAAAAOqr2qKcXb4PeOxzI0KqQq0fiiSi"  // remplace avec ta clé
										  });
										}
										$("#preCommande").modal("show");
									});

									// Réinitialiser le captcha à chaque fermeture du modal
									$("#preCommande").on("hidden.bs.modal", function () {
									  if (typeof grecaptcha !== "undefined" && captchaWidget !== undefined) {
										grecaptcha.reset(captchaWidget);
									  }
									});
								}

                            }
                        );

                        $.post('includes/get_ref_option.php',{ idopt : idopt },
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

<p style="margin-left:8px">2. Envoyez le justificatif de paiement &agrave;&nbsp;<a href="mailto:Offre@samfi.tn" style="color:#1155cc" target="_blank">Offre@samfi.tn</a>&nbsp;avec votre Nom, Pr&eacute;nom ,N&deg;de t&eacute;l&eacute;phone et adresse email&nbsp;; ainsi que le Nom,Pr&eacute;nom et adresse email du b&eacute;n&eacute;ficiaire de la commande si ce n&rsquo;est&nbsp;pas&nbsp;pour vous</p>

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
            max:125356.244,
            values:[0.000, 125356.244],
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
    
    def test_samfi_tn(self):
        html = samfi_tn_products_page()
        result = self.detector.detect(html=html, page_url="https://www.samfi.tn/fr/categories/produit-siderurgique/fer-marchand/")
        print(result.confidence_score)
        print(result.products)
        assert result.is_product_list is True