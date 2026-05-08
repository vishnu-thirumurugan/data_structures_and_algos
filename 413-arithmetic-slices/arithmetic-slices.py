class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        left = 0
        res = 0 
        right = 2
        while right < n:
            if nums[right-1] - nums[right-2] == nums[right]- nums[right-1]:
                if left == None:
                    left = right - 2

                res += right-left-1
            
            else:
                left = None

            right += 1

        return res
            



        