import itertools

def generate_ascii_combinations(n):
    ascii_characters = ''.join(chr(i) for i in range(32, 127))
    combinations = itertools.product(ascii_characters, repeat=n)
    for combination in combinations:
        yield ''.join(combination)

n = 3
for combination in generate_ascii_combinations(n):
    print(combination)


# import sys
# print(sys.getdefaultencoding())
# print(chr(126))
