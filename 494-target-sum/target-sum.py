class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # convert this problem to knapsack --> gemini
        # divide the array into two sets of positive and negative numbers
        # p + n = total sum
        # p-n = target
        # 2p = total sum + target
        # p = (total sum)+ target /2
        n = len(nums)
        total_sum = sum(nums)
        # edge cases --> early exit 
        if (total_sum + target)% 2 != 0:
            return 0

        if target > total_sum:
            return 0

        p = (target+total_sum)//2 #--> this is your new target

        # states --> (index, current_target)
        # memo = {}
        @lru_cache(None)
        def helper(index, curr_target):
            # base case
            if index == n:
                if curr_target == 0: return 1
                return 0

            ways = helper(index+1, curr_target)
            print(index+1, curr_target)
            if nums[index] <= curr_target:
                ways += helper(index+1, curr_target-nums[index]) # leave or take

            return ways

        return helper(0,p)



            


            

            
        