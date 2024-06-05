def initial_permutation(text):
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    return ''.join([text[i - 1] for i in ip])

def inverse_initial_permutation(text):
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    return ''.join([text[i - 1] for i in ip_inv])

def expand_and_permute(right):
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    return ''.join([right[i - 1] for i in ep])

def xor(bits1, bits2):
    return ''.join(['0' if b1 == b2 else '1' for b1, b2 in zip(bits1, bits2)])

def sbox(input, sbox):
    row = int(input[0] + input[3], 2)
    col = int(input[1] + input[2], 2)
    return '{:02b}'.format(sbox[row][col])

def f_k(left, right, subkey):
    expanded_permuted = expand_and_permute(right)
    xored = xor(expanded_permuted, subkey)
    left_half, right_half = xored[:4], xored[4:]
    sbox_0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    sbox_1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    sbox_output = sbox(left_half, sbox_0) + sbox(right_half, sbox_1)
    p4 = [2, 4, 3, 1]
    p4_result = ''.join([sbox_output[i - 1] for i in p4])
    return xor(left, p4_result)

def sdes_encrypt(plaintext, key):
    # Key scheduling (generating two subkeys)
    key_permutation_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    key_permutation_8 = [6, 3, 7, 4, 8, 5, 10, 9]
    key_p10 = ''.join([key[i - 1] for i in key_permutation_10])
    key_left, key_right = key_p10[:5], key_p10[5:]
    # Perform one left shift
    key_left = key_left[1:] + key_left[0]
    key_right = key_right[1:] + key_right[0]
    subkey1 = ''.join([key_left[i - 1] for i in key_permutation_8])
    # Perform two left shifts
    key_left = key_left[2:] + key_left[:2]
    key_right = key_right[2:] + key_right[:2]
    subkey2 = ''.join([key_left[i - 1] for i in key_permutation_8])
    
    # Initial Permutation
    permuted_text = initial_permutation(plaintext)
    left, right = permuted_text[:4], permuted_text[4:]
    # First round of Fk
    left = f_k(left, right, subkey1)
    # Switch function
    left, right = right, left
    # Second round of Fk
    left = f_k(left, right, subkey2)
    # Combine left and right
    combined_text = left + right
    # Inverse Initial Permutation
    ciphertext = inverse_initial_permutation(combined_text)
    return ciphertext

# Example usage:
plaintext = "01010010" + "01000111"  # RG in binary
key1 = "0110110010"
key2 = "0110010010"

ciphertext1_part1 = sdes_encrypt(plaintext[:8], key1)
ciphertext1_part2 = sdes_encrypt(plaintext[8:], key1)
ciphertext2_part1 = sdes_encrypt(plaintext[:8], key2)
ciphertext2_part2 = sdes_encrypt(plaintext[8:], key2)

ciphertext1 = ciphertext1_part1 + ciphertext1_part2
ciphertext2 = ciphertext2_part1 + ciphertext2_part2

# Calculate Hamming distance
def hamming_distance(bin1, bin2):
    return sum(b1 != b2 for b1, b2 in zip(bin1, bin2))

print("Ciphertext 1:", ciphertext1)
print("Ciphertext 2:", ciphertext2)
print("Hamming Distance:", hamming_distance(ciphertext1, ciphertext2))
