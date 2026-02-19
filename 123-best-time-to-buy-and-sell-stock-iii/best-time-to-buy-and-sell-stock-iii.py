class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memoization solution 
        n = len(prices)
        memo = {}
        def helper(ind,buy,cap):
            if ind == n or cap == 0:
                return 0
            if (ind, buy, cap) in memo:
                return memo[(ind,buy,cap)]
            if buy == 1:
                memo[(ind,buy,cap)] =  max(
                    -prices[ind] + helper(ind+1,0,cap), # buy
                    0 + helper(ind+1,1,cap) # not buy
                )
                return memo[(ind,buy,cap)]

            else: # sell
                memo[(ind,buy,cap)] =  max(
                    prices[ind] + helper(ind+1,1,cap-1), # sell:transaction completed
                    0 + helper(ind+1,0,cap) # not selling
                )
                return memo[(ind,buy,cap)]

        return helper(0,1,2) # 2 transactions allowed


        