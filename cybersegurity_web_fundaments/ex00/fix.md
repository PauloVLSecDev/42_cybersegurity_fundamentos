A correcao tem como objetvivo fazer com que o programa nao aceite ` o que gera um escape do javascript tambem nao fazer com que o programa gere uma <script> toda fez que um input for passado
	tambem o document.cookie esta sendo passado no javascript sendo que deveria estar sendo executado e definido no backend do site. assim o tornando mais seguro que o atual

	abaixo segue o codigo corrigido

	<!DOCTYPE html>
	<html>
	<head>
    <title>Vulnerable XSS Example</title>
	</head>
	<body>
    <h1>XSS Vulnerability Example</h1>
    <p>This is a vulnerable page with an XSS vulnerability.</p>
    <form>
        <label for="inputText">Enter some text:</label>
        <input type="text" id="inputText">
        <button type="button" onclick="displayText()">Submit</button>
    </form>
    <div id="output"></div>
    <script>
        function displayText() {
            var userInput = document.getElementById("inputText").value;
            document.getElementById("output").textContent = userInput;

        }
    	</script>

    	<div id="cookieOutput"></div>
	</body>
	</html>

nos escolhemos o elemento 
