class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0 
        maxSum = 0
        currSum = 0

        for right in range(len(nums)):
            while nums[right] in nums[left:right]:
                currSum -= nums[left]
                left += 1

            currSum += nums[right]
            maxSum = max(maxSum, currSum)

        return maxSum 