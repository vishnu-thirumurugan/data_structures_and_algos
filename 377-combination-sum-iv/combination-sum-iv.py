class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(t):
            if t == 0:
                return 1
            if t < 0:
                return 0 

            if t in memo:
                return memo[t]

            count = 0
            for num in nums:
                count += dfs(t-num)

            memo[t] = count
            return memo[t]

        return dfs(target)

             
        