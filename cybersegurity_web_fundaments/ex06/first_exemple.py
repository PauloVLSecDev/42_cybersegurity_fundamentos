

import base64

# 1. Os bytes intermediários que o PadBuster encontrou na última execução.
 intermediate_hex = "e1c5601fabeffbe30dab31d9acf95c1a"
intermediate_bytes = bytes.fromhex(intermediate_hex)

# 2. O plaintext que desejamos, com o padding PKCS#7 correto.
desired_plaintext = b'admin'
padding_len = 16 - len(desired_plaintext)
desired_plaintext_padded = desired_plaintext + bytes([padding_len]) * padding_len

# 3. A mágica do XOR para calcular o IV forjado.
forged_iv_bytes = bytearray()
for i in range(16):
        forged_iv_bytes.append(intermediate_bytes[i] ^ desired_plaintext_padded[i])

        # 4. O criptograma (cookie ID) pode ser um bloco nulo, já que os bytes intermediários
        #    foram calculados com base nele.
        ciphertext_bytes = b'\x00' * 16

        # 5. Codificar os resultados em Base64 para usar nos cookies.
        cookie_id = base64.b64encode(ciphertext_bytes).decode('utf-8')
        cookie_token = base64.b64encode(forged_iv_bytes).decode('utf-8')

        # --- Exibir o resultado final ---
        print("="*50)
        print("[+] PAYLOAD FINAL GERADO COM SUCESSO!")
        print("Use estes cookies no seu navegador para obter a flag:")
        print(f"\n    Cookie 'ID'    ->  {cookie_id}")
        print(f"    Cookie 'token' ->  {cookie_token}")
        print("="*50)
# 1. Os bytes intermediários que o PadBuster encontrou na última execução.
intermediate_hex = "e1c5601fabeffbe30dab31d9acf95c1a"
intermediate_bytes = bytes.fromhex(intermediate_hex)

# 2. O plaintext que desejamos, com o padding PKCS#7 correto.
desired_plaintext = b'admin'
padding_len = 16 - len(desired_plaintext)
desired_plaintext_padded = desired_plaintext + bytes([padding_len]) * padding_len

# 3. A mágica do XOR para calcular o IV forjado.
forged_iv_bytes = bytearray()
for i in range(16):
        forged_iv_bytes.append(intermediate_bytes[i] ^ desired_plaintext_padded[i])

        # 4. O criptograma (cookie ID) pode ser um bloco nulo, já que os bytes intermediários
        #    foram calculados com base nele.
        ciphertext_bytes = b'\x01' * 16

        # 5. Codificar os resultados em Base64 para usar nos cookies.
        cookie_id = base64.b64encode(ciphertext_bytes).decode('utf-8')
        cookie_token = base64.b64encode(forged_iv_bytes).decode('utf-8')

        # --- Exibir o resultado final ---
        print("="*50)
        print("[+] PAYLOAD FINAL GERADO COM SUCESSO!")
        print("Use estes cookies no seu navegador para obter a flag:")
        print(f"\n    Cookie 'ID'    ->  {cookie_id}")
        print(f"    Cookie 'token' ->  {cookie_token}")
        print("="*50)
