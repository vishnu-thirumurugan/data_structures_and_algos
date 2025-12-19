class Solution:
    def findCircleNum(self, provinces: List[List[int]]) -> int:
        n = len(provinces)
        visited = [0]*n

        
        count = 0 # number of provinces
        for i in range(n): # one complete pass for disconnected components
            
            if visited[i] == 0: # then only traverse
                count += 1
                q = deque([i])
                visited[i] = 1
                
                while q:
                    node = q.popleft()
                    for nei in range(n):
                        if provinces[node][nei] == 1 and visited[nei] == 0:
                            visited[nei] = 1
                            q.append(nei)

        return count


        


        