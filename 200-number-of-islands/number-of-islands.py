class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # dfs way 
        row, col = len(grid), len(grid[0])

        visited = [[0]*col for _ in range(row)]

        count = 0

        directions = [(0,1), (1,0), (0, -1), (-1,0)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1  # each connected component is an island

                    q = deque([(i,j)])
                    visited[i][j] = 1

                    while q:
                        r,c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0<= nr < row and 0 <= nc < col and grid[nr][nc] == '1' and visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                q.append((nr,nc))

        return count


        