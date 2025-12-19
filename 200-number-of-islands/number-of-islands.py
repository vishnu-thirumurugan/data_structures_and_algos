class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # dfs way 
        row, col = len(grid), len(grid[0])

        visited = [[0]*col for _ in range(row)]

        count = 0

        def dfs(r,c):
            visited[r][c] = 1
            directions = [(0,1), (1,0), (0, -1), (-1,0)]

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < row and 0<= nc < col and visited[nr][nc] == 0 and grid[nr][nc] == '1':
                    dfs(nr, nc)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1  # each connected component is an island
                    dfs(i, j)

        return count

        