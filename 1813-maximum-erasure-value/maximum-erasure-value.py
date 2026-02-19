class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0 
        maxSum = 0
        currSum = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                currSum -= nums[left]
                seen.remove(nums[left])
                left += 1

            seen.add(nums[right])
            currSum += nums[right]
            maxSum = max(maxSum, currSum)

        return maxSum 