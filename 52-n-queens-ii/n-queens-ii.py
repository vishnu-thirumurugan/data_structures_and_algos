class Solution:
    def totalNQueens(self, n: int) -> int:
        # previous submission will be more intuitive
        # this one is optimized

        rows = [0]*n
        diag1 = [0]*(2*n-1)
        diag2 = [0]*(2*n-1)

        self.count = 0 

        def backtrack(col):
            if col == n:
                self.count += 1
                return

            for row in range(n):
                if not rows[row] and not diag1[row+col] and not diag2[n-1+col-row]:
                    rows[row] = 1
                    diag1[row+col] = 1
                    diag2[n-1+col-row] = 1
                    backtrack(col+1)
                    rows[row] = 0
                    diag1[row+col] = 0
                    diag2[n-1+col-row] = 0
            
        backtrack(0)

        return self.count




        