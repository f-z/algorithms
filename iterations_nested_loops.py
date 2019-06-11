from itertools import product

for p in product("ab", repeat=4):
    print("".join(p))
