class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque(node for node in range(n) if indegree[node] == 1 )
 

        while q:
            answer = list(q)
            for i in range(len(q)):
                node = q.popleft()

                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        return answer

        




            

        

        