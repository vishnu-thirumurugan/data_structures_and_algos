class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        for i in range(1,n-1):
            if (not nums[i] == nums[i-1] and not nums[i] == nums[i+1]):
                return nums[i]

        if nums[0] != nums[1]:
            return nums[0]

        return nums[-1]
            