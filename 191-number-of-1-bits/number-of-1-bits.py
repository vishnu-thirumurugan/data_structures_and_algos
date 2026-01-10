class Solution:
    def hammingWeight(self, n: int) -> int:
        # time complexity o(number of 1s)
        count = 0
        while n:
            n = n & (n-1)
            count+= 1
        return count

        