class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        counter = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                counter += 1
            else:
                counter = 1

            if counter <= 2:
                nums[ptr] = nums[i]
                ptr += 1

        return ptr
