class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque([])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        print(fresh)
        level = 0
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in ([0,1], [1,0],[-1,0],[0,-1]):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))

            level += 1
        print(fresh)
        return level if fresh == 0 else -1







                

        

         
        