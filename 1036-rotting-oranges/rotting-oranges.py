class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # not reachability
        # this is propogation over time
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        fresh = 0
        # multi source bfs --> identify the sources 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        # bfs 
        level = 0
        while q and fresh > 0:
            size = len(q) #   level wise
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in ((0,1), (1,0), (-1,0), (0,-1)):
                    nr, nc = r+dr, c+dc
                    if 0<= nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            level += 1

        return level if fresh == 0 else -1

                

        

         
        