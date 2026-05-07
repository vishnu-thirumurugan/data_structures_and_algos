class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        ans = 0
        cSum = 0
        freq = defaultdict(int)

        for right in range(n):
            # add right
            cSum += nums[right]
            freq[nums[right]] += 1

            # if needed remove left
            if right-left+1 > k:
                cSum -= nums[left]
                freq[nums[left]] -= 1

                # this will help in calculating len of dict
                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            # update ans 
            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, cSum)

        return ans

        

            


        