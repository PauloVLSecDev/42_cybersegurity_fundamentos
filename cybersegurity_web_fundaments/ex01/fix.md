Como corrigir a vulnerabilidade CSRF
Para corrigir a vulnerabilidade CSRF, é crucial garantir que nenhuma solicitação seja processada sem a devida validação.

A principal técnica para isso é o uso de tokens CSRF. O servidor deve gerar um novo token único para cada sessão de usuário. Este token é inserido em formulários HTML ou cabeçalhos HTTP de solicitações POST. Quando a solicitação é enviada, o servidor valida se o token recebido corresponde ao que foi gerado para aquela sessão específica.

Dessa forma, um atacante não consegue forjar uma solicitação maliciosa, pois ele precisaria ter um token válido, que é único para cada sessão do usuário. Para aumentar a segurança, o token deve expirar após um determinado tempo, impedindo sua reutilização.

Outra medida de segurança importante é a validação da origem da solicitação. O servidor pode verificar o cabeçalho Referer ou Origin para garantir que a solicitação POST venha do mesmo domínio do site. Isso ajuda a impedir acessos remotos de URLs externas e não autorizadas.
