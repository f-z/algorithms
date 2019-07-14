import itertools

# Ordered combinations (permutations) with repetitions
x = [1, 2, 3, 4, 5, 6]
print([p for p in itertools.product(x, repeat=2)])

# Unordered combinations with repetitions
# All the combinations with repetitions of n types of things taken k at a time
from itertools import combinations_with_replacement
n, k = 'iced jam plain'.split(), 2
print(list(combinations_with_replacement(n, k)))
print(len(list(combinations_with_replacement(range(10), 3))))

from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBL", 4):
    print("".join(c))

# Ordered (permutations), without repetitions
from itertools import permutations
for a in permutations("123456789", 4):
    print("".join(a))

print(len(list(permutations("123456789", 4))))

# Permutations with repetitions
x = [1, 2, 3, 4]
print(len([p for p in itertools.product(x, repeat=9)]))

import itertools as it
list_positive_integers_fixed_sum = []
# Combinations with repetitions
for d in it.product(range(10), repeat=4):
    if sum(d) == 10:
        list_positive_integers_fixed_sum.append(d)

print(len(list_positive_integers_fixed_sum))

print(itertools.permutations("123456789", 4).__sizeof__())
