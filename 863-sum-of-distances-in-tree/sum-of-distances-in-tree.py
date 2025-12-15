class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        # create graph from edges
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subtree_size = [1] * n
        sum_dist = [0] * n

        # in first pass calculate sum_dist[0] and subtree length
        def dfs_post_order(node, parent):
            for child in adj[node]:
                if  child != parent:
                    dfs_post_order(child, node)

                    subtree_size[node] += subtree_size[child]
                    sum_dist[node] +=  subtree_size[child] + sum_dist[child] # aggregate till root

        # first pass will calculate only the sum_dist for the sub tree with node as root
        # for all other node, we need to make one more pass to update

        dfs_post_order(0, -1) # bottom up

        # the other pass can be either bds or dfs
        q = deque([(node,0) for node in adj[0]]) # first genration children in queue init

        while q:
            node, parent = q.popleft()
            # update answer
            sum_dist[node] = sum_dist[parent] - subtree_size[node] + (n - subtree_size[node])
            # for a node, all the nodes in its subtree, becomes a step closer --> subtract
            # all the nodes, outside becomes a step farther --> add

            for child in adj[node]:
                if child != parent:
                    q.append((child, node))

        return sum_dist


        