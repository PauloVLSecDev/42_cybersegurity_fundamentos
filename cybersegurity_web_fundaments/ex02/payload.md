esse sao os payloads possiveis mas vale lembrar que a como e possivel injetar python e por consequencia ter acesso ao servidor linux podemos executar shell script 
podendo causar estragos criticos ao sistema como deletar todas os arquivos todos os templates etc, roubar todos os dados criar arquivos dentre outros
 
explicando usamos o {{}} para executa comandos o problema que o jinja2 e poderoso demais ja a url_for e uma funcao do flask que tem como objetivo criar novas rotasd de url para cada template assim evitando que uma rola url possa ser harcoded ou seja escrito de forma fixa contudo neste caso usamos ela para ter acesso ao ao modulos disponivels para execucao de servidor nesrte casdo o 

__globals__ quando chamamos esta funcao juntamente com a url_for obtemos a modulos python3 chamaod na aplicacao e neste caso comom tesmos a funcao popen podemos ultizar ela.
para isso nos refenciamos ao modulo ['os'] que nos permite interagit com o sistema operacional e neste caso usamos a fucnao .popen que nos permite executar comandos do sistema operacional esta seja um cat ou um kill como nos exemples de payload abaixo  


{{ url_for.__globals__['os'].popen('cat /etc/passwd').read() }}

{{ url_for.__globals__['os'].popen('rm -rf /etc).read() }}

{{ url_for.__globals__['os'].popen('rm -rf *').read() }}

{{ url_for.__globals__['os'].popen('kill -2 1').read()}}
