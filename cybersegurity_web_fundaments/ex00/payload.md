document.getElementById("cookieOutput").innerHTML = `Cookie value: ${document.cookie}`;     
	
neste exeplo de patyload usamos getElementBuId("cookieOutput) para selecionar o id que queremos neste caso e da div que possui o id cookieOutput de modo que ao selecionar este elemento

nos atribuimos a ele uma varial neste caso  a document.cookie contudo nos indicamos para o getElement que queremos tambem pegar qualquer elemento HTML dentro desta variavel com .innerHTML

mais alguns payloads interessantes 

document.write(<h1> THIS IS SITE WAS HACKED </h1>) 

<a href="https://profile.intra.42.fr/dont/exist/"> LINK TOTALMENTE SEGURO </a>

aqui um exeplo de como poderiamos acresentar informacoes falsas em um site com propositos maliciososos
