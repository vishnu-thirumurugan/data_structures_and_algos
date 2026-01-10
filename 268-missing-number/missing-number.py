class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n*(n+1)*0.5) - sum(nums)