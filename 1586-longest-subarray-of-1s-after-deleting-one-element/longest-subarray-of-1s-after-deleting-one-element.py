class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        ans = 0 
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[left]  == 0:
                    zeroCount -= 1
                left += 1
            ans = max(ans, right-left) # one element is deleted
        
        return ans
        