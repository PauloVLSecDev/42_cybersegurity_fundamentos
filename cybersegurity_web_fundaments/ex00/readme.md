
A vulnerabilidade que está presente no exercício é um XSS autoencapsulado, ou seja, ela se autoencapsula criando em torno de cada input um

	<script> código malicioso </script>

logo neste caso não é necessário usar o <script></script>, apenas o código malicioso, e o programa já entende como um script válido.

	Cenários de exploração:

O primeiro cenário de exploração seria para roubo de tokens gerados a partir do roubo do cookie, que neste caso estava inseguro.

O segundo seria a alteração do HTML do site, por exemplo, modificando algum elemento e assim gerando um phishing. Como estamos falando de uma falha XSS stored encapsulado, todas as alterações feitas no HTML da página podem ser vistas por todos os usuários do site. Desse modo, fazemos com que a vítima clique em algum link na página.

