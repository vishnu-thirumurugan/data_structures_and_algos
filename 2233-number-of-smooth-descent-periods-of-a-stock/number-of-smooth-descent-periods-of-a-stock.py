class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 1
        streak = 1

        for i in range(1,n):
            if prices[i-1] - prices[i] == 1: # smooth descent
                streak += 1
            else:
                streak = 1
            ans  += streak

        return ans
