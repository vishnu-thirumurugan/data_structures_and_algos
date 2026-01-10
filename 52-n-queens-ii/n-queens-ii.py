class Solution:
    def totalNQueens(self, n: int) -> int:
        # arrays to check previously filled queens
        pure_left = [0]*n
        left_upper_diagonal = [0]*(2*n-1)
        left_lower_diagonal = [0]*(2*n-1)

        row = col = n
        board = [['.']*n for _ in range(n)]
        self.count = 0 

        def backtrack(col,board,pure_left, left_lower_diagonal, left_upper_diagonal):
            if col == n: # queens are placed in all cols
                self.count += 1
                return

            for row in range(n):
                if (board[row][col] == '.' 
                and pure_left[row] == 0 
                and left_lower_diagonal[row+col] == 0 
                and left_upper_diagonal[n-1+col-row] == 0):
                    pure_left[row] = 1
                    left_lower_diagonal[row+col] = 1
                    left_upper_diagonal[n-1+col-row] = 1
                    board[row][col] = 'Q'
                    # fill next column
                    backtrack(col+1,board,pure_left, left_lower_diagonal, left_upper_diagonal)
                    pure_left[row] = 0
                    left_lower_diagonal[row+col] = 0
                    left_upper_diagonal[n-1+col-row] = 0
                    board[row][col] = '.'


        backtrack(0,board,pure_left, left_lower_diagonal, left_upper_diagonal)
        return self.count





        