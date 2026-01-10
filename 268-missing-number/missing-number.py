class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bit manipulation way 
        n = len(nums)
        xor_all = 0

        for i in range(n):
            xor_all ^= i        # expected_array [0 to n]
            xor_all ^= nums[i]  # original_array

        # xor with n finally to complete expected array
        xor_all ^= n

        return xor_all