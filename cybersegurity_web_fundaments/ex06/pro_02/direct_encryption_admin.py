#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import requests

def create_admin_token(secret_key):
    """
    Cria um token que descriptografa para 'admin' usando a chave secreta
    """
    print("=== CRIANDO TOKEN ADMIN COM CHAVE CONHECIDA ===")
    print(f"Chave secreta: {secret_key}")
    
    # Dados que queremos criptografar
    plaintext = b'admin'
    
    # Adiciona padding PKCS7 para completar 16 bytes
    padding_length = 16 - (len(plaintext) % 16)
    padded_plaintext = plaintext + bytes([padding_length]) * padding_length
    
    print(f"Plaintext: {plaintext}")
    print(f"Padded plaintext: {padded_plaintext} (hex: {padded_plaintext.hex()})")
    
    # Gera IV aleatório
    iv = get_random_bytes(16)
    
    # Criptografa usando AES-128-CBC
    cipher = AES.new(secret_key.encode('utf-8'), AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_plaintext)
    
    # Codifica em base64
    ciphertext_b64 = base64.b64encode(ciphertext).decode()
    iv_b64 = base64.b64encode(iv).decode()
    
    print(f"\nToken gerado:")
    print(f"ID (ciphertext): {ciphertext_b64}")
    print(f"token (IV): {iv_b64}")
    
    return ciphertext_b64, iv_b64

def create_multiple_admin_tokens(secret_key, count=5):
    """
    Cria múltiplos tokens admin para aumentar as chances
    """
    tokens = []
    
    for i in range(count):
        print(f"\n--- Token {i+1} ---")
        cipher_b64, iv_b64 = create_admin_token(secret_key)
        tokens.append((cipher_b64, iv_b64))
    
    return tokens

def test_token(base_url, cipher_b64, iv_b64):
    """
    Testa um token no servidor
    """
    cookies = {
        'ID': cipher_b64,
        'token': iv_b64
    }
    
    try:
        response = requests.get(base_url, cookies=cookies, timeout=10)
        content = response.text
        
        if "ERROR!" in content:
            return "ERROR", "Erro de padding/descriptografia"
        elif "Hello Nice to see you!" in content:
            if any(flag in content.lower() for flag in ['flag{', 'ctf{', 'flag:', 'flag=']):
                return "FLAG", content
            else:
                return "SUCCESS_NO_FLAG", "Login bem-sucedido mas sem flag visível"
        elif "login" in content.lower():
            return "LOGIN_PAGE", "Ainda na página de login"
        else:
            return "UNKNOWN", f"Resposta inesperada: {content[:200]}..."
            
    except Exception as e:
        return "NETWORK_ERROR", str(e)

def verify_decryption(secret_key, cipher_b64, iv_b64):
    """
    Verifica o que um token descriptografa localmente
    """
    try:
        ciphertext = base64.b64decode(cipher_b64)
        iv = base64.b64decode(iv_b64)
        
        cipher = AES.new(secret_key.encode('utf-8'), AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        
        # Remove padding
        padding_length = decrypted[-1]
        plaintext = decrypted[:-padding_length]
        
        print(f"Descriptografia local:")
        print(f"  Raw: {decrypted.hex()}")
        print(f"  Plaintext: {plaintext}")
        print(f"  ASCII: {''.join(chr(b) if 32 <= b <= 126 else f'\\x{b:02x}' for b in plaintext)}")
        
        return plaintext
        
    except Exception as e:
        print(f"Erro na descriptografia: {e}")
        return None

def main():
    # SUBSTITUA PELA CHAVE SECRETA REAL
    secret_key = "this_is_key_you_do_not_know"  # Coloque a chave real aqui
    base_url = "http://localhost:8085/"
    
    print("=== GERAÇÃO DE TOKEN ADMIN COM CHAVE CONHECIDA ===")
    
    if secret_key == "SUBSTITUA_PELA_CHAVE_REAL":
        print("❌ ERRO: Você precisa substituir a chave secreta!")
        print("Abra o script e coloque a chave real na variável 'secret_key'")
        return
    
    # Cria múltiplos tokens
    tokens = create_multiple_admin_tokens(secret_key, 3)
    
    print("\n" + "="*60)
    print("TOKENS PARA TESTAR:")
    print("="*60)
    
    for i, (cipher_b64, iv_b64) in enumerate(tokens, 1):
        print(f"\nToken {i}:")
        print(f"curl -H \"Cookie: ID={cipher_b64}; token={iv_b64}\" {base_url}")
        
        # Verifica localmente
        verify_decryption(secret_key, cipher_b64, iv_b64)
        
        # Testa no servidor
        print("Testando no servidor...")
        status, message = test_token(base_url, cipher_b64, iv_b64)
        print(f"Resultado: {status} - {message}")
        
        if status == "FLAG":
            print("\n🎉 FLAG ENCONTRADA!")
            print(message)
            break
        elif status == "SUCCESS_NO_FLAG":
            print("✅ Login bem-sucedido! Verifique a resposta completa:")
            response = requests.get(base_url, cookies={'ID': cipher_b64, 'token': iv_b64})
            print(response.text)
    
    print(f"\n{'='*60}")
    print("Se nenhum token funcionou, verifique:")
    print("1. A chave secreta está correta?")
    print("2. O servidor está acessível?")
    print("3. A implementação do servidor está conforme esperado?")

# Versão simplificada para teste rápido
def quick_test():
    secret_key = "this_is_key_you_do_not_know"  # Substitua pela chave real
    
    print("=== TESTE RÁPIDO ===")
    
    # Cria apenas um token
    cipher_b64, iv_b64 = create_admin_token(secret_key)
    
    print(f"\nComando curl para testar:")
    print(f'curl -H "Cookie: ID={cipher_b64}; token={iv_b64}" http://localhost:8085/')

if __name__ == "__main__":
    # Para teste completo, use main()
    # Para apenas gerar o comando curl, use quick_test()
    
    choice = input("Digite 'q' para teste rápido ou Enter para teste completo: ").strip().lower()
    
    if choice == 'q':
        quick_test()
    else:
        main()
