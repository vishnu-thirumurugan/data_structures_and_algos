class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        if n == 0 or n == 1:
            memo[n] = n
            return n 

        if n in memo:
            return memo[n]

        memo[n-1] = self.fib(n-1)
        memo[n-2] = self.fib(n-2)

        return memo[n-1] + memo[n-2]

        