class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # graph dp  --> dfs + memoization
        m, n = len(matrix), len(matrix[0])

        memo = {}

        directions = [[0,1], [0, -1], [1,0], [-1, 0]]

        def dfs(r, c):
            if (r,c) in memo:
                return memo[(r,c)]
            dist = 1
            # explore all 4 dir
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    dist = max(dist, 1 + dfs(nr,nc))

            memo[(r,c)] = dist
            return dist

            
        # check for every cell
        self.longest_dist = 1
        for i in range(m):
            for j in range(n):
                self.longest_dist = max(self.longest_dist, dfs(i,j))
        print(memo)
        return self.longest_dist
