class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @lru_cache(None)
        def helper(index, curr_target):
            # reached req amount
            if curr_target == 0:
                return 1
            # reached end / got more than amount
            if index == n or curr_target < 0:
                return 0

            return helper(index+1, curr_target) + helper(index, curr_target - coins[index]) 
            # leave and move or take and stay

        return helper(0, amount)