class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 0/1 knapsack kind off 
        # take or leave pattern

        s = sum(nums)

        if s % 2 != 0:
            return False
        
        n = len(nums)

        target = s // 2

        @lru_cache(None)
        def helper(idx, curr_target):
            # if u reach the end of array
            if idx == n:
                return False
            # if u get the target
            if curr_target == 0:
                return True

            if curr_target < 0: return False

            # main recursion

            # leave
            if helper(idx+1, curr_target): # no change in target,as u didnt take 
                return True

            # take
            if nums[idx] <= curr_target:
                if helper(idx+1, curr_target - nums[idx]):
                    return True

            return False # if both branches were false 

        return helper(0,target)

        