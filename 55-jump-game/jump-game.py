class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # can i reach idx i (dp) --> how for I can reach from current idx (greedy)
        n = len(nums)
        max_reach = 0 

        for i in range(n):
            # you are in a state, which is unreachable
            if i > max_reach:
                return False

            # update max_reach
            max_reach = max(max_reach, i + nums[i])

            # if you reach or cross last index, return true
            if max_reach > n-1:
                return True 

        return True


