n = 10
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j < k:
                count += 1

# 10C3
print(count)

n = 1000
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j < k:
                count += 1

# 1000C3
print(count)
