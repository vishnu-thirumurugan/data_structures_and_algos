class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left = 0
        ans = 0 
        n = len(nums)
        distinctCount = len(set(nums))
        # print(distinctCount)
        count = {}

        for right in range(n):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while len(count) == distinctCount:
                ans += n-right
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1     

        return ans

        