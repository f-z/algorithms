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
