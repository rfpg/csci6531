def hamming_distance(str1, str2):
    """Calculate the Hamming distance between two binary strings."""
    assert len(str1) == len(str2)
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

#ciphertexts
ciphertext1 = "101011100111001010001001010101110010111101111010"
ciphertext2 = "00100100100000001001101011111111001001000001100011111100"
ciphertext3 = "0111101011010010010011101101001011110101"

#add padding so we can compare
ciphertext1_padded = ciphertext1.ljust(len(ciphertext2), '0')
ciphertext3_padded = ciphertext3.ljust(len(ciphertext2), '0')

#calculate hamming distances
distance_1_2 = hamming_distance(ciphertext1_padded, ciphertext2)
distance_1_3 = hamming_distance(ciphertext1_padded, ciphertext3_padded)
distance_2_3 = hamming_distance(ciphertext2, ciphertext3_padded)

print(f"Distance between Ciphertext 1 and Ciphertext 2: {distance_1_2}")
print(f"Distance between Ciphertext 1 and Ciphertext 3: {distance_1_3}")
print(f"Distance between Ciphertext 2 and Ciphertext 3: {distance_2_3}")
