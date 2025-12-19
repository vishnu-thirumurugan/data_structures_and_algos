class Solution:
    def findCircleNum(self, provinces: List[List[int]]) -> int:
        n = len(provinces)
        visited = [0]*n

        def dfs(node):
            visited[node] = 1
            for nei in range(n):
                if provinces[node][nei] == 1 and visited[nei] == 0:
                    dfs(nei)

        count = 0
        # all provinces
        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs(i)

        return count

        


        