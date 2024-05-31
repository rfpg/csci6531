import itertools
import string

# plaintext = "hello"
# key = "bbb"

# def vigenere_encrypt_ascii(plaintext, key):
#     encrypted_text = []
#     key_length = len(key)
#     for i, char in enumerate(plaintext):
#         key_char = key[i % key_length]
#         encrypted_char = chr((ord(char) - 32 + ord(key_char) - 32) % 95 + 32)
#         encrypted_text.append(encrypted_char)
#     return ''.join(encrypted_text)

# ciphertext = vigenere_encrypt_ascii(plaintext, key)

# problem 1 ciphertext
# ciphertext = """Xx,#x,vw.))z$m9)qz||9v{~5v~yr/#6.%6&v{!z){~{})59-r.}){%m35!~~p"*)#$).}n9(j(|n9%o9E7LJ2N5t#"x!(j'))AE7PL2JF7IG)&w29vw}5!#$p9)yz$)){)OE2JE99xn(*r'z},z|9=;M><R5r(>79iq~5vz x,~}35x 5|*zl#z|9}j0z)}v{%5o~v}"z{-C)m}n9wr&")#))&%w!A).}r(5j(y)"%x%zmG5]"zr,5o~z}9}j0z)1zk{~w!5k~*!~zw9vu&5o)+{9*x~)79Vu&5|*zl#z|9v{~5o#)qFzj.z{-A)|v}|}r(|).}n9&{~/){/)}~ #$p9{{)#).}n9)~,{j|z7"""

# problem 2 ciphertext
ciphertext = """X+wu~)*|q,o4&)ox0xy'}%|u~*};0{s(x~x{0)u}|"}4y$*+q(s$&)*%|vmy$5s#0*ry0-y'|y84Q(m|qzy! |swq"*y'~ny~xo4$+q{u)~(0*ru%5m$##y'q$~4v~}|y$q4(v}4!(kw%~}yt5s#0Vxwyzx)0Zq.!*64`z|*<5U$#zk4q$n4Y$n}qA*v&**)xz*(%(y#wz})0*|ut~~} $*|q)*'u#k}~zn4y$*Wx~xu0vxx0_k%q$64(}o'u5s)0(ous}ox0xy"}z|wyvvA$xk!u5vy'zv4y$*( #o4q(ou$C*]~5Tu!vx@0xy'}%|u~**zy)r}~|*}$5mu|"ox0+uuy5k#t5s(0&o'v%|"uy*v*5k4v~}|u(wu~5u# -x4q)*u~5 (x%8"""

common_words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
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
    decrypted_text_lower = decrypted_text.lower()
    for word in common_words:
        word_lower = word.lower()
        if f" {word_lower} " in decrypted_text_lower or f"{word_lower} " in decrypted_text_lower or f" {word_lower}" in decrypted_text_lower or f"{word_lower}." in decrypted_text_lower or f"{word_lower}," in decrypted_text_lower:
            return True
    return False

def is_readable_ascii(text):
    return all(32 <= ord(char) <= 126 for char in text)

def score_decrypted_text(decrypted_text):
    # Calculate a score based on the frequency of common words
    word_list = decrypted_text.split()
    common_word_count = sum(word.lower() in common_words for word in word_list)
    return common_word_count

def try_all_keys(ciphertext, key_length):
    best_score = -1
    best_decrypted_text = ""
    best_key = ""
    for key in generate_ascii_combinations(key_length):
        decrypted_text = vigenere_decrypt(ciphertext, key)
        if is_readable_ascii(decrypted_text):
            score = score_decrypted_text(decrypted_text)
            if score > best_score:
                best_score = score
                best_decrypted_text = decrypted_text
                best_key = key
    if best_score > 0:
        print(f"Best Key: {best_key}\nDecrypted Text: {best_decrypted_text}\n")

key_length = 4  # Set the key length
try_all_keys(ciphertext, key_length)
