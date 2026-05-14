class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        # exactly k = atmost(k) - atmost(k-1)

        def atmost(k):
            left = 0 
            ans = 0
            count = {}

            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right],0) + 1

                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                ans += right - left + 1

            return ans

        return atmost(k) - atmost(k-1)

            
        