class Solution:
    
    def climbStairs(self, n: int) -> int:

        prev = 1
        curr = 1

        for i in range(2,n+1):
            temp = curr
            curr = curr + prev
            prev = temp

        return curr