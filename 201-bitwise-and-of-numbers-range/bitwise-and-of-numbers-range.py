class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # if you you use commutative property, you will get TLE, coz of constraints
        # you should no the property of n & n-1 to solve this
        while left < right:
            right = right & (right - 1)
        return right

        