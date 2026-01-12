class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        mod = 10**9 + 7
        @lru_cache(None)
        def recursion(idx, n_rem, profit_rem):
            if idx == m: # you have exhausted groups
                return profit_rem <= 0

            # skip current one
            ans = (recursion(idx+1, n_rem, profit_rem))%mod

            # take current one
            if group[idx] <= n_rem:
                # if you didnt use the max function, cache will explode in memory 
                ans = (ans + recursion(idx+1, n_rem - group[idx], max(profit_rem - profit[idx],0))) % mod

            return ans

        return (recursion(0, n, minProfit))%mod



        