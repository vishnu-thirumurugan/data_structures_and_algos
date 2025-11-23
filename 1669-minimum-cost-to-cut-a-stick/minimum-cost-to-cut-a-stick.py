class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # cutting at middle wont help 
        # cut made now decides future cost --> explore all ways

        # similar to burst baloons --> learnt from gemini chats (Interval dp problem)

        # normalise the cuts array 
        cuts = [0] + sorted(cuts) + [n]

        memo = {}

        def solve(i,j): # min cost to cut stick starting at cuts[i] and ending at cuts[j]
            if (i,j) in memo:
                return memo[(i,j)]
            if j - i == 1: # cannot cut between length of 1
                return 0
            min_cost = float('inf')
            for k in range(i+1, j):
                # Cost = Length of current stick + cost of left side + cost of right side
                current_cost = (cuts[j] - cuts[i]) + solve(i,k) + solve(k,j)
                min_cost = min(min_cost, current_cost)

            memo[(i,j)] = min_cost
            return memo[(i,j)]
            
        m = len(cuts)
        # solve for full stick
        return solve(0, m-1)
        