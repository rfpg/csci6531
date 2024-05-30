import itertools
import string

def generate_ascii_combinations(n):
    ascii_characters = string.printable[:-6]  # Exclude non-printable characters
    combinations = itertools.product(ascii_characters, repeat=n)
    for combination in combinations:
        yield ''.join(combination)

# Example usage
n = 3  # Change this value to generate combinations of different lengths
for combination in generate_ascii_combinations(n):
    print(combination)
