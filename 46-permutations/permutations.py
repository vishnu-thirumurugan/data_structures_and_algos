class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # swapping technique
        # no extra space
        # most optimal (learnt from chat gpt and tuf)

        n = len(nums)
        res = []

        def backtrack(start):
            if start == n:
                # no more swapping 
                res.append(nums.copy())
                return

            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        backtrack(0)
        return res




            
        