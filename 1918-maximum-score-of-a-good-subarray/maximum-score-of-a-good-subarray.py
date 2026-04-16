class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # minimum element of the subarray is the one which controls the score
        # instead of trying all subarrays --> start from k and expand outwards
        # expand to the side with maximum value greedily --> to keep minimum as large as possible
        n = len(nums)
        currMin = nums[k]
        i = j = k
        ans = currMin

        while i > 0 or j < n-1:
            if i == 0:
                j += 1
            elif j == n-1:
                i -= 1
            elif nums[i-1] > nums[j+1]:
                i -= 1
            else:
                j += 1

            currMin = min(currMin, nums[i], nums[j])
            ans = max(ans, currMin*(j-i+1))

        return ans

        # you can also solve this by stack

        