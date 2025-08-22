
A vulnerabilidade encontrada e um SSRF (Server-side request Forgery) + LFI local file inclusion  no diagrama abaixo um exemplo de com e seu funcionamento 
com essa vulnerabilidade podemos explorar o servidor pois nao ha validacao dos tipos da url como http ou https e neste caso tambem aceita o tipo file:// o que nos possibilita 
acessar informacoes sensiveis dos arquivos do servidor como etc/shadow, etc/hostname/ etc/passwd 

┌───────────────────┐
│  Seu Navegador    │
│  (curl / fetch)   │
└────────┬──────────┘
         │
         │ 1️⃣ Envia requisição HTTP
         │    para o servidor vulnerável
         ▼
┌──────────────────────────────────────┐
│  Servidor Vulnerável                 │
│  (Ex: /fetch?url=file:///etc/passwd) │
└────────┬─────────────────────────────┘
         │
         │ 2️⃣ Interpreta a URL fornecida pelo usuário
         │    Detecta o esquema file://
         ▼
┌───────────────────────────┐
│  Sistema de Arquivos do   │
│  Servidor (Linux, etc.)   │
└────────┬──────────────────┘
         │
         │ 3️⃣ Acesso ao arquivo local
         │    /etc/passwd
         ▼
┌───────────────────────────┐
│ Conteúdo do arquivo       │
│ /etc/passwd               │
└────────┬──────────────────┘
         │
         │ 4️⃣ O servidor devolve
         │    o conteúdo como resposta HTTP
         ▼
┌───────────────────┐
│  Seu Navegador    │
│  Recebe o conteúdo│
└───────────────────┘

