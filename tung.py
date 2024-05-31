import itertools
import string

plaintext = "hello"
key = "bbb"

def vigenere_encrypt_ascii(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    for i, char in enumerate(plaintext):
        key_char = key[i % key_length]
        encrypted_char = chr((ord(char) - 32 + ord(key_char) - 32) % 95 + 32)
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

ciphertext = vigenere_encrypt_ascii(plaintext, key)

common_words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "hello",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at"
]

def generate_ascii_combinations(n):
    ascii_characters = string.printable[:-6]  # Printable ASCII characters
    combinations = [''.join(comb) for comb in itertools.product(ascii_characters, repeat=n)]
    return combinations

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char) + 95) % 95 + 32)
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

def contains_common_word(decrypted_text, common_words):
    for word in common_words:
        if word in decrypted_text:
            return True
    return False

def is_readable_ascii(text):
    return all(32 <= ord(char) <= 126 for char in text)

def try_all_keys(ciphertext, key_length):
    for key in generate_ascii_combinations(key_length):
        decrypted_text = vigenere_decrypt(ciphertext, key)
        if contains_common_word(decrypted_text, common_words):
            print(f"Key: {key}\nDecrypted Text: {decrypted_text}\n")

key_length = 3  #set the key length
try_all_keys(ciphertext, key_length)
