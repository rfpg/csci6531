def count_coincidences(text, offset):
    """
    Count the number of coincidences when the text is compared with an offset version of itself.
    
    Args:
        text (str): The ciphertext to analyze.
        offset (int): The offset to compare against.
    
    Returns:
        int: The number of coincidences.
    """
    coincidences = 0
    for i in range(len(text) - offset):
        if text[i] == text[i + offset]:
            coincidences += 1
    return coincidences

def find_likely_key_lengths(text, max_key_length):
    """
    Find the likely key lengths based on the number of coincidences for each offset.
    
    Args:
        text (str): The ciphertext to analyze.
        max_key_length (int): The maximum key length to consider.
    
    Returns:
        list: A list of tuples containing the key length and the number of coincidences.
    """
    key_length_coincidences = []
    for key_length in range(1, max_key_length + 1):
        coincidences = count_coincidences(text, key_length)
        key_length_coincidences.append((key_length, coincidences))
    return key_length_coincidences

# Given ciphertext
ciphertext = """Xx,#x,vw.))z$m9)qz||9v{~5v~yr/#6.%6&v{!z){~{})59-r.}){%m35!~~p"*)#$).}n9
(j(|n9%o9E7LJ2N5t#"x!(j'))AE7PL2JF7IG)&w29vw}5!#$p9)yz$)){)OE2JE99xn
(*r'z},z|9=;M><R5r(>79iq~5vz x,~}35x 5|*zl#z|9}j0z)}v{%5o~v}"z{-C)m}
n9wr&")#))&%w!A).}r(5j(y)"%x%zmG5]"zr,5o~z}9}j0z)1zk{~w!5k~*!~zw9vu&5o)
+{9*x~)79Vu&5|*zl#z|9v{~5o#)qFzj.z{-A)|v}|}r(|).}n9&{~/){/)}~ #$p9{{)
#).}n9)~,{j|z7"""

# Define the maximum key length to consider
max_key_length = 20

# Find the likely key lengths based on the number of coincidences
likely_key_lengths = find_likely_key_lengths(ciphertext, max_key_length)

# Print the number of coincidences for each key length
print("Key Length - Number of Coincidences")
for key_length, coincidences in likely_key_lengths:
    print(f"{key_length} - {coincidences}")


