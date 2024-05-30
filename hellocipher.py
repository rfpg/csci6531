def vigenere_encrypt_ascii(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    for i, char in enumerate(plaintext):
        key_char = key[i % key_length]
        encrypted_char = chr((ord(char) - 32 + ord(key_char) - 32) % 95 + 32)
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

def vigenere_decrypt_ascii(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char) + 95) % 95 + 32)
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

plaintext = "hello"
key = "bb"
ciphertext = vigenere_encrypt_ascii(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = vigenere_decrypt_ascii(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
