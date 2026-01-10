class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = [0] * n
        diag1 = [0] * (2 * n - 1)   # row + col
        diag2 = [0] * (2 * n - 1)   # n - 1 + col - row
        self.count = 0

        def backtrack(col):
            if col == n:
                self.count += 1
                return

            for row in range(n):
                d1 = row + col
                d2 = n - 1 + col - row
                if not rows[row] and not diag1[d1] and not diag2[d2]:
                    rows[row] = diag1[d1] = diag2[d2] = 1
                    backtrack(col + 1)
                    rows[row] = diag1[d1] = diag2[d2] = 0

        backtrack(0)
        return self.count
