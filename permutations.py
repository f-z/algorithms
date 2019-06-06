from itertools import permutations

for p in permutations("abcdef", 3):
    print("".join(p))
