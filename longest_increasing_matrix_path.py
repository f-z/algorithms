# Longest increasing path in a matrix, across all directions
def longest_increasing_path(dp, a, n, m, x, y):
    # If value not calculated yet
    if dp[x][y] < 0:
        result = 0

        # End state
        if x == n - 1 and y == m - 1:
            dp[x][y] = 1
            return dp[x][y]

        # If value greater than above cell -> move down
        if x < n - 1 and a[x][y] < a[x + 1][y]:
            result = max(result, 1 + longest_increasing_path(dp, a, n,
                                                             m, x + 1, y))

        # If value greater than below cell
        if x > 0 and a[x][y] < a[x - 1][y]:
            result = max(result, 1 + longest_increasing_path(dp, a, n,
                                                             m, x - 1, y))

        # If value greater than left cell
        if y + 1 < m and a[x][y] < a[x][y + 1]:
            result = max(result, 1 + longest_increasing_path(dp, a, n,
                                                             m, x, y + 1))

        # If value greater than right cell
        if y > 0 and a[x][y] < a[x][y - 1]:
                result = max(result, 1 + longest_increasing_path(dp, a, n,
                                                                 m, x, y - 1))

        dp[x][y] = result
    return dp[x][y]


n = 4
m = 4

matrix = [[1, 4, 5, 4],
          [2, 3, 4, 7],
          [3, 6, 5, 8],
          [4, 7, 8, 9]]

dp = [[-1 for i in range(len(matrix[0]))]
      for i in range(len(matrix))]

print(longest_increasing_path(dp, matrix, n, m, 0, 0))
