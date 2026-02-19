class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        dp = [[[0]*(k+1) for _ in range(2)] for i in range(n+1)]

        for ind in range(n-1, -1, -1): # indices fall
            for buy in range(2):
                for cap in range(1,k+1):

                    if buy == 1:
                        dp[ind][buy][cap] = max(
                            -prices[ind] + dp[ind+1][0][cap], # buy
                            0 + dp[ind+1][1][cap]             # not buy
                        )

                    else: # sell
                        dp[ind][buy][cap] = max(
                            prices[ind] + dp[ind+1][1][cap-1], # sold
                            0 + dp[ind+1][0][cap]
                        )

        return dp[0][1][k]