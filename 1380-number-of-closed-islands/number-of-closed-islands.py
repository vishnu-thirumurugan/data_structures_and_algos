class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            if i < 0 and j < 0 or i > m-1 or j > n-1 or grid[i][j] == 1:
                return
            # mark visited
            grid[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        # remove the boundary water
        for i in range(m):
            for j in [0,n-1]:
                if grid[i][j] == 0:
                    dfs(i,j)

        for j in range(n):
            for i in [0, m-1]:
                if grid[i][j] == 0:
                    dfs(i,j)

        # inside islands
        count = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i,j)

        return count

        

        