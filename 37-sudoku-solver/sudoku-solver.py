class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empty = []

        # initialize and fill the sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r,c))
                else:
                    num = board[r][c]
                    row[r].add(num)
                    col[c].add(num)
                    box[(r//3)*3 + c//3].add(num)
        

        def backtrack(idx):
            if idx == len(empty):
                return True # this means u have filled all the boxes

            r,c = empty[idx]

            for num in '123456789':
                if num not in row[r] and num not in col[c] and num not in box[(r//3)*3 + c//3]:
                    board[r][c] = num
                    row[r].add(num)
                    col[c].add(num)
                    box[(r//3)*3 + c//3].add(num)

                    if backtrack(idx+1):
                        return True

                    # backtrack
                    board[r][c] = '.'
                    row[r].remove(num)
                    col[c].remove(num)
                    box[(r//3)*3 + c//3].remove(num)

            return False # not finding a number between 1 to 9 to fill a box

        backtrack(0)

            
            





        