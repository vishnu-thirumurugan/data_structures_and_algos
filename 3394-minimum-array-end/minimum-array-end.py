class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        bit = 0

        while k:
            if (x & (1 << bit)) == 0:
                if k & 1:
                    x |= (1 << bit)
                k >>= 1
            bit += 1

        return x
