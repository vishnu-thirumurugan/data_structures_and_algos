class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        memo = {}

        def dp(i,j):
            if j >= n or i >= n:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == t[j]:
                memo[(i,j)] = 1 + dp(i+1, j+1)
            else:
                memo[(i,j)] = max(dp(i+1,j), dp(i,j+1))

            return memo[(i,j)]

        return dp(0,0)


        dp = [[0*n] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, n):
                if s[i] == t[j]:
                    dp[i][j] = 2 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n-1][n-1]


