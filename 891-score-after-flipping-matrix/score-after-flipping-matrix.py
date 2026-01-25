class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        for r in range(row):
            if grid[r][0] == 0:
                # flip
                for c in range(col):
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0

        for c in range(col):
            count_1 = 0
            for r in range(row):
                if grid[r][c] == 1:
                    count_1 += 1

            if count_1 < math.ceil(row/2):
                # flip
                for r in range(row):
                    if grid[r][c] == 0:
                            grid[r][c] = 1
                    else:
                        grid[r][c] = 0
        # print(grid)
        score = 0
        # now count the numbers row wise
        for nums in grid:
            score += int(''.join(list(map(str,nums))),2)

        return score

            
        