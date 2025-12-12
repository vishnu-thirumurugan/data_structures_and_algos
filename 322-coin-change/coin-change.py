class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # unbounded knapsack problem
        n = len(coins)

        @lru_cache(None)
        def helper(curr_target):
            if curr_target == 0:
                return 0 # we hve already achieved target
            
            if curr_target < 0:
                return float('inf') # unable to achieve target

            best = float('inf')
            for coin in coins:
                best = min(best, 1 + helper(curr_target-coin))
            return best

        res = helper(amount)
        if res == float('inf'):
            return -1
        return res
            
        