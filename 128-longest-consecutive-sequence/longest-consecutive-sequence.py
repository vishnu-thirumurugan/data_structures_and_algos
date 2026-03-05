class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        currentLength = 0
        maxLength = 0

        for i in range(len(nums)):
            if nums[i-1] + 1 == nums[i]:
                currentLength += 1

            else:
                currentLength = 1

            maxLength = max(maxLength, currentLength)

        return maxLength
        
        