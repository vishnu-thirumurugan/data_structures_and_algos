class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # --- Pass 1: Calculate Left Products ---
        # Initialize with 1 (neutral multiplication element)
        current_prefix = 1
        for i in range(n):
            ans[i] = current_prefix
            current_prefix = current_prefix * nums[i]

        # --- Pass 2: Calculate Right Products & Final Result ---
        # Initialize with 1
        current_suffix = 1
        for i in range(n - 1, -1, -1):
            # Multiply the stored Left Product by the current Right Product
            ans[i] = ans[i] * current_suffix
            # Update the running suffix product
            current_suffix = current_suffix * nums[i]

        return ans