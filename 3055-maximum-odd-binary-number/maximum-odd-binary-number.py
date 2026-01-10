class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # clean and optimized way is to take advantage of string
        ones = s.count('1')
        n = len(s)

        return '1'*(ones-1) + '0'*(n-ones)+ '1'
        