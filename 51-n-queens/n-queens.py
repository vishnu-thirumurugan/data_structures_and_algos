class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 3(n) memory way
        board = [['.'] * n for _ in range(n)]
        left_side = [0]*n
        left_upper_diagonal = [0]*(2*n - 1)
        left_lower_diagonal = [0]*(2*n - 1)
        res = []

        def backtrack(col, board, left_side, left_upper_diagonal, left_lower_diagonal):
            if col == n:
                res.append([''.join(row.copy()) for row in board])
                return

            # place queens column wise --> while not possible simply backtrack (other base case is handled inherently)
            for row in range(n):
                if (left_side[row] == 0 and
                    left_lower_diagonal[row+col] == 0 and 
                    left_upper_diagonal[n-1 + col - row] == 0): # safer choice

                    board[row][col] = 'Q' # take the string (row) and put Q in that column
                    left_side[row] = 1
                    left_lower_diagonal[row+col] = 1
                    left_upper_diagonal[n-1+col-row] = 1
                    backtrack(col + 1, board, left_side, left_upper_diagonal, left_lower_diagonal) # try to place queen in next col by recursion
                    # while backtracking remove queen
                    board[row][col] = '.' 
                    left_side[row] = 0
                    left_lower_diagonal[row+col] = 0
                    left_upper_diagonal[n-1+col-row] = 0


        backtrack(0,board,left_side, left_upper_diagonal, left_lower_diagonal)
        return res





        