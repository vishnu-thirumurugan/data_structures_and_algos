class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n-2):
            if nums[i] == 0: # flip
                ans  += 1

                # flip 3 consecutives
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1

        return ans if nums[-1] == 1 and nums[-2] == 1 else -1