class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # if the curretn bit is effectively 0, we flip i:i+k
        # if current bit is effectively 0 and if i+k < n, we return -1

        n = len(nums)
        # even flips --> 0 --> not flipped
        # odd flips --> 1 --> flipped
        isFlipped = 0                # whether the current bit is flipped
        previousExpiredFlips = [0]*n # to remove the effect of previous flips which are out of range [i-k]
        ans = 0

        for i in range(n):

            # remove the effect of previous flip
            if i >= k:
                isFlipped ^= previousExpiredFlips[i-k]

            # if current bit is effectively 0
            if nums[i] == isFlipped:  # 0==0 means it was 0 and you never flipped, 1==1 means it was 1 and you flipped it
                # check if its not possible to flip
                if i+k > n:
                    return -1
                
                # if not flip it
                ans += 1
                isFlipped ^= 1 
                previousExpiredFlips[i] = 1

        return ans

        