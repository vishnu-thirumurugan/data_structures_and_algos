class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        # union find way 
        rows = len(grid)
        cols = len(grid[0])

        # union declarations
        parent = {}
        rank = {} # subtree size 

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        
        def union(x, y):
            root_x, root_y = find(x), find(y)

            if root_x == root_y: # already same set --> no merge req
                return 0
            
            if rank[root_x] >= rank[root_y]:
                parent[root_y] = root_x
                rank[root_x] += root_y

            else:
                parent[root_x] = root_y
                rank[root_y] += root_x

            return 1

        count = 0 # number of initial sets
        # intialize parent and rank matrix and count
        for r in range(rows):
            for c in range(cols):
                idx = r*cols + c
                if grid[r][c] == '1':
                    parent[idx] = idx
                    rank[idx] = 1
                    count += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    idx = r * cols + c
                    for dr, dc in [[1, 0],[0,1]]: # see only right and down --> reduces redundant calls
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            nidx = nr* cols + nc
                            count -= union(idx, nidx)

        return count


            




        