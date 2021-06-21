#!/bin/python3
def minimum_range_activations(locations):
    n = len(locations)
    dp = [-1] * n

    for i in range(n):
        left_index = max(i - locations[i], 0)
        right_index = min(i + (locations[i] + 1), n)
        dp[left_index] = max(dp[left_index], right_index)
    # Initializations, starting range
    count = 1
    right_index = dp[0]
    next_index = dp[i]
    for i in range(n):
        next_index = max(next_index, dp[i])
        # Reaching end of current range
        if (i == right_index):
            # Adding to count
            count += 1
            # Moving to rightmost index found thus far
            right_index = next_index

    return count

a = [2, 1, 1]
print(minimum_range_activations(a))