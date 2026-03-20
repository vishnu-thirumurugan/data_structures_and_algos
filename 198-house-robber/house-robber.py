class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 0/1 knapsack
        memo = {}
        def dp(i):
            if i in memo: return memo[i]
            if i < 0:
                return 0
            robbing = nums[i] + dp(i-2)
            skip_rob = dp(i-1)

            memo[i] = max(robbing, skip_rob)

            return memo[i]
        return dp(n-1)
        
        