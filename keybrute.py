import itertools

def generate_ascii_combinations(n):
    ascii_characters = ''.join(chr(i) for i in range(32, 127))  # ASCII range 32 to 126
    combinations = itertools.product(ascii_characters, repeat=n)
    for combination in combinations:
        yield ''.join(combination)

# Example usage
n = 3  # Change this value to generate combinations of different lengths
for combination in generate_ascii_combinations(n):
    print(combination)


# import sys
# print(sys.getdefaultencoding())
# print(chr(126))
