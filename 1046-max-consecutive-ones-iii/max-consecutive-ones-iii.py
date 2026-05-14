class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        maxOnes = 0
        flipCounts = 0

        for right in range(n):
            if nums[right] == 0:
                flipCounts += 1
                
            while flipCounts > k:
                if nums[left] == 0:
                    flipCounts -= 1
                
                left += 1

            maxOnes = max(maxOnes, right-left+1)

        return maxOnes

                
                
        