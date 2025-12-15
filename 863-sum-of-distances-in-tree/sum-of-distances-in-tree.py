class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # Brute force is to claculate from each node iusing dfs
        # O(N * N)

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subtree_size = {}
        answer = [0] * n

        def dfs(u, pr):

            subtree_size[u] = 1
            for v in adj[u]:
                if v != pr:
                    dfs(v, u)

                    subtree_size[u] += subtree_size[v]
            # return size

        dfs(0, -1)
        answer[0] = sum(subtree_size.values()) - subtree_size[0]

        q = deque([(node, 0) for node in adj[0]])

        while q:
            node, pr = q.popleft()
            answer[node] = answer[pr] - subtree_size[node] + (n - subtree_size[node])

            for v in adj[node]:
                if v != pr:
                    q.append((v, node))

        return answer

        

