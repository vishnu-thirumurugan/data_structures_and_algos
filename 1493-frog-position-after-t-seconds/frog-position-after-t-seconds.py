class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent, probability, time):

            children = [nei for nei in adj[node] if nei != parent]

            if node == target:
                # if time has reached or its the leaf node
                if time == t or not children:
                    return probability
                return 0.0

            if time == t or not children:
                return 0.0

            for child in children:
                res = dfs(child, node, probability/len(children), time + 1)
                if res != 0:
                    return res

            return 0

        return dfs(1, -1, 1.0, 0)


        
