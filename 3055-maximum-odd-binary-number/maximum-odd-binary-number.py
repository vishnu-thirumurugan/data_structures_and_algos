class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        n = len(s)
        num = int(s, 2)
        while num:
            if num & 1:
                count += 1
            num //= 2 # u can also use right shift operator
        
        res = ''
        # keep one '1' at the end and others at the begining
        # put the zeros in between
        for _ in range(count-1):
            res += '1'
        for _ in range(n-count):
            res += '0'
        
        res += '1'

        return res
        