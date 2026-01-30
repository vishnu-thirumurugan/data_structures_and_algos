class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore majority vote 
        # o(n) and o(1)
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if candidate == num else -1

        return candidate
        