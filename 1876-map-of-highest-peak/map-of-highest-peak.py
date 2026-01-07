class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]*cols for i in range(rows)]

        q = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r,c))
                    visited[r][c] = 1
                    grid[r][c] = 0

                else:
                    grid[r][c] = 1

        level = 0
        
        while q:
            size = len(q)
            level += 1

            for _ in range(size):
                r,c = q.popleft()
                for dr, dc in ((1,0), (0,1), (-1, 0), (0, -1)):
                    nr, nc = r+dr, c+dc
                    # dont alter if neighbor is water
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and visited[nr][nc]== 0:
                        grid[nr][nc] = level
                        q.append((nr,nc))
                        visited[nr][nc] = 1

        return grid
                        





        