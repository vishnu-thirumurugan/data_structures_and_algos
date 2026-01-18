class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n & - n finds last set bit 
        if n == 0: return False
        return n - (n & - n) == 0
        