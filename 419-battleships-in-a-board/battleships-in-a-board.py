class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        
        def dfs(r,c):
            if visited[r][c]=='1':
                return
            for dr, dc in ((0,1),(1,0), (0,-1), (-1,0)):
                nr, nc = r+dr, c+dc
                if 0 <=nr < m and 0 <= nc < n and visited[nr][nc] == 0 and board[nr][nc] == 'X':
                    visited[nr][nc] = 1
                    dfs(nr, nc)
        
        visited = [[0]*n for _ in range(m)]
        count  = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    if board[i][j] == 'X':
                        count += 1
                        dfs(i,j)
                        # visited[i][j] = 1

        return count


        