class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        # idea
        # water leaks from boundary --> can leak from multiple boundary cells
        # multi source bfs --> with heap (lower boundary leaks first)

        heap = []

        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]

        # take all the boundaries
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    heapq.heappush(heap, (grid[r][c], r, c))
                    visited[r][c] = 1

        # multi source bfs based on heap 
        # early leak --> measure first 
        result = 0

        while heap:
            height, r, c = heapq.heappop(heap)
            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0:
                    heapq.heappush(heap, (max(grid[nr][nc], height), nr, nc)) # after trapping water
                    visited[nr][nc] = 1
                    if height > grid[nr][nc]:
                        result += height - grid[nr][nc]


        return result

                
            
