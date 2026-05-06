class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def dfs(num, length):
            if length == n:
                res.append(num)
                return

            lastDigit = num % 10
            nextPossible = set([lastDigit+k, lastDigit-k])

            for digit in nextPossible:
                if 0 <= digit <= 9:
                    dfs(num*10 + digit, length + 1)

        for i in range(1,10):
            dfs(i,1)

        return res

        