class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxElement = max(nums)
        return nums.index(maxElement)
        