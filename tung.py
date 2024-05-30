import itertools
import string

ciphertext = ("Xx,#x,vw.))z$m9)qz||9v{~5v~yr/#6.%6&v{!z){~{})59-r.}){%m35!~~p\"*)#$).}n9\n"
              "(j(|n9%o9E7LJ2N5t#\"x!(j'))AE7PL2JF7IG)&w29vw}5!#$p9)yz$)){)OE2JE99xn\n"
              "(*r'z},z|9=;M><R5r(>79iq~5vz x,~}35x 5|*zl#z|9}j0z)}v{%5o~v}\"z{-C)m}\n"
              "n9wr&\")#))&%w!A).}r(5j(y)\"%x%zmG5]\"zr,5o~z}9}j0z)1zk{~w!5k~*!~zw9vu&5o)\n"
              "+{9*x~)79Vu&5|*zl#z|9v{~5o#)qFzj.z{-A)|v}|}r(|).}n9&{~/){/)}~ #$p9{{)\n"
              "#).}n9)~,{j|z7")

common_words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at"
]

def generate_ascii_combinations(n):
    ascii_characters = ''.join(chr(i) for i in range(32, 127)) #printable char range
    return itertools.product(ascii_characters, repeat=n)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
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
    for key_tuple in generate_ascii_combinations(key_length):
        key = ''.join(key_tuple)
        decrypted_text = vigenere_decrypt(ciphertext, key)
        if is_readable_ascii(decrypted_text) and contains_common_word(decrypted_text, common_words):
            print(f"Key: {key}\nDecrypted Text: {decrypted_text}\n")



key_length = 4  #use kasiski to identify likely key length and try one at a time
try_all_keys(ciphertext, key_length)
