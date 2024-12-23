from collections import deque


class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1

        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
