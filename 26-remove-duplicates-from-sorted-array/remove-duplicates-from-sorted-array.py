class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0

        for i in range(len(nums)):
            if nums[i] != nums[ptr]:
                # found a new number
                ptr += 1
                nums[ptr] = nums[i]
        return ptr + 1