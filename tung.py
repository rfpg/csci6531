import itertools
import string

ciphertext = "ifmmp"  # key is "bb"

common_words = [
    "the", "be", "to", "of", "and", "", "in", "that", "have", "hel",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at"
]

def generate_ascii_combinations(n):
    ascii_characters = ''.join(chr(i) for i in range(32, 127))  # printable char range
    return itertools.product(ascii_characters, repeat=n)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char) + 95) % 95 + 32)
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

def contains_common_word(decrypted_text, common_words):
    normalized_text = decrypted_text.lower()
    print(normalized_text)
    for word in common_words:
        if f' {word} ' in f' {normalized_text} ':
            return True
    return False

def is_readable_ascii(text):
    return all(32 <= ord(char) <= 126 for char in text)

def try_all_keys(ciphertext, key_length):
    for key_tuple in generate_ascii_combinations(key_length):
        key = ''.join(key_tuple)
        decrypted_text = vigenere_decrypt(ciphertext, key)
        if is_readable_ascii(decrypted_text) and contains_common_word(decrypted_text, common_words):
            print(f"Key: {key}\nDecrypted Text: {decrypted_text}\n")
            return  # Stop after finding the first valid key

key_length = 2  # Use kasiski to identify likely key length and try one at a time
try_all_keys(ciphertext, key_length)
