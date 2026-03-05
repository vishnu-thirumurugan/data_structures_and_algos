class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        currentLength = 1
        maxLength = 1

        for i in range(len(nums)):

            if nums[i-1] == nums[i]:
                continue

            if nums[i-1] + 1 == nums[i]:
                currentLength += 1

            else:
                currentLength = 1

            maxLength = max(maxLength, currentLength)

        return maxLength
        
        