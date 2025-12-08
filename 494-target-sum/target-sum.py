class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def helper(idx, curr_sum):
            # base case
            if idx == n:
                if curr_sum == target:
                    return 1
                return 0

            output = (helper(idx + 1, curr_sum + nums[idx]) + 
                        helper(idx + 1, curr_sum - nums[idx]))

            return output

        return helper(0,0)


            

            

            
        