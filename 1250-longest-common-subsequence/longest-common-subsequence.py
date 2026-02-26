class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        memo = {}

        def dp(i,j):
            if i == m or j == n:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            if s[i] == t[j]:
                # inc length
                memo[(i,j)] = 1 + dp(i+1, j+1)
            else:
                memo[(i,j)] = max(dp(i+1,j), dp(i, j+1))

            return memo[(i,j)]

        return dp(0,0)
