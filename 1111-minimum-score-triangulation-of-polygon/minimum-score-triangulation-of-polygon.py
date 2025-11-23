class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # similar to minimum cost to cut a stick 
        # an interval dp problem

        # first form a triangle with an index
        # then solve the left sub problem, and right sub separately

        n = len(values)

        memo = {}

        def solve(i,j):
            if j - i < 2: # u cannot form a triangle
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            min_score = float('inf')
            # Try every possible vertex k between i and j to form the triangle (i, k, j)
            for k in range(i+1, j):
                # k is the peak for a base (i,j) to form a rectangle
                # Cost = Left Polygon + Right Polygon + Triangle(i, k, j)
                current_score = values[i] * values[k] * values[j] + solve(i,k) + solve(k,j)
                # solve(i,k) --> i, k will be the base and u will search for new peak inside
                min_score = min(min_score, current_score)

            memo[(i,j)] = min_score
            return memo[(i,j)]

        return solve(0,n-1) # solve for 0, n-1 as base