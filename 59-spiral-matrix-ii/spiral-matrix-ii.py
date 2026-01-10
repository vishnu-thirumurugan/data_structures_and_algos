class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]

        dirs = [(0,1), (1,0), (0, -1), (-1, 0)] # R--> D--> L-->U
        d = 0
        r = c = 0

        for num in range(1, n*n+1):
            matrix[r][c] = num

            nr, nc = r + dirs[d][0], c + dirs[d][1]

            # change directions as per constraints
            if not (0<=nr<n and  0<=nc<n and matrix[nr][nc] == 0):
                d = (d+1)%4
                nr, nc = r + dirs[d][0], c + dirs[d][1]

            r, c = nr, nc

        return matrix




        