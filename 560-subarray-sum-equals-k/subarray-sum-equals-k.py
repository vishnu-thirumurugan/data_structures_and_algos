class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        current_sum = 0
        res = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum == k:
                res += 1

            if current_sum - k in prefix_sum:
                res += prefix_sum[current_sum-k]

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return res

        
        