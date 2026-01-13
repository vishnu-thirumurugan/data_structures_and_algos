class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        val = [1] + nums + [1]
        n = len(val)

        dp = [[0]*n for _ in range(n)]

        for length in range(2, n):  # solve for lesser lenght first
        # this will give you (i,k) and (k,j) in dp
        # which u can use later
            for i in range(n-length):
                j = i + length
                # bursting baloons in between
                for k in range(i+1,j):
                    coins = max(dp[i][j], dp[i][k] + val[i]*val[k]*val[j] + dp[k][j])
                    if coins > dp[i][j]:
                        dp[i][j] = coins

        return dp[0][n-1]







