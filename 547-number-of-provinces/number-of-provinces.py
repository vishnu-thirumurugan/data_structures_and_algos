class Solution:
    def findCircleNum(self, provinces: List[List[int]]) -> int:
        # union find way (DSU)

        n = len(provinces)  # number of nodes
    
        parent = [i for i in range(n)] # init parent of it is self

        count = n # initially all the nodes are separate componests

        # rank or size
        rank = [1] * n  # initially their size will be 1 (think of it like subtree size)

        def find(x): # iterative function to find root of x
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x  

        def union(x,y):
            rootx, rooty = find(x), find(y)

            # no merge, if their roots are same (same components)
            if rootx == rooty:
                return 0

            # merge operation
            if rank[x] >= rank[y]:
                parent[rooty] = rootx
                rank[rootx] += rank[rooty]
            
            else:
                parent[rootx] = rooty
                rank[rooty] += rank[rootx]

            return 1


        for r in range(n):
            for c in range(r+1, n): # only upper triangular is enough
                if provinces[r][c]:
                    count -= union(r,c)

        return count

       
        


        


        