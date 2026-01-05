class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set to make the o(1) lookup
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        # initialize and fill
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    row[r].append(num)
                    col[c].append(num)
                    box[3*(r//3)+ (c//3)].append(num)

        for i in range(9):
            counter_row = Counter(row[i])
            counter_col = Counter(col[i])
            counter_box = Counter(box[i])

            if any(v > 1 for v in counter_row.values()):
                return False

            if any(v > 1 for v in counter_col.values()):
                return False

            if any(v > 1 for v in counter_box.values()):
                return False

        return True


        




        