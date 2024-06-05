def permute(sequence, table):
    return [sequence[i-1] for i in table]

def shift_left(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def generate_subkeys(key):
    permuted_key = permute(key, [3, 5, 2, 7, 4, 10, 1, 9, 8, 6])
    
    left, right = permuted_key[:5], permuted_key[5:]
    left, right = shift_left(left, 1), shift_left(right, 1)
    subkey1 = permute(left + right, [6, 3, 7, 4, 8, 5, 10, 9])
    left, right = shift_left(left, 2), shift_left(right, 2)
    subkey2 = permute(left + right, [6, 3, 7, 4, 8, 5, 10, 9])
    
    return subkey1, subkey2

def sbox(input_bits, sbox):
    row = (input_bits[0] << 1) + input_bits[3]
    col = (input_bits[1] << 1) + input_bits[2]
    return [int(x) for x in format(sbox[row][col], '02b')]

def fk(bits, subkey):
    left, right = bits[:4], bits[4:]
    expanded_right = permute(right, [4, 1, 2, 3, 2, 3, 4, 1])
    xor_result = xor(expanded_right, subkey)
    
    left_sbox_output = sbox(xor_result[:4], [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]])
    right_sbox_output = sbox(xor_result[4:], [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]])
    
    sbox_output = left_sbox_output + right_sbox_output
    permuted_sbox_output = permute(sbox_output, [2, 4, 3, 1])
    left = xor(left, permuted_sbox_output)
    
    return left + right

def sdes_encrypt(plaintext, key):
    initial_permutation = permute(plaintext, [2, 6, 3, 1, 4, 8, 5, 7])
    subkey1, subkey2 = generate_subkeys(key)
    
    result = fk(initial_permutation, subkey1)
    result = result[4:] + result[:4]
    result = fk(result, subkey2)
    
    ciphertext = permute(result, [4, 1, 3, 5, 7, 2, 8, 6])
    return ciphertext

def binary_str_to_list(binary_str):
    return [int(bit) for bit in binary_str]

def main():
    plaintext = '0101001001000111' #my initials RG
    key1 = '0110110010'
    key2 = '0110010010'
    
    plaintext_bits = binary_str_to_list(plaintext)
    key1_bits = binary_str_to_list(key1)
    key2_bits = binary_str_to_list(key2)
    
    ciphertext1 = sdes_encrypt(plaintext_bits, key1_bits)
    ciphertext2 = sdes_encrypt(plaintext_bits, key2_bits)
    
    ciphertext1_str = ''.join(map(str, ciphertext1))
    ciphertext2_str = ''.join(map(str, ciphertext2))
    
    bit_difference = sum(c1 != c2 for c1, c2 in zip(ciphertext1, ciphertext2))
    
    print(f'Ciphertext 1: {ciphertext1_str}')
    print(f'Ciphertext 2: {ciphertext2_str}')
    print(f'Number of differing bits: {bit_difference}')

if __name__ == "__main__":
    main()
