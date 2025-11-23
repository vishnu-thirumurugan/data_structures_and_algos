class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # cutting at middle wont help 
        # cut made now decides future cost --> explore all ways

        # similar to burst baloons --> learnt from gemini chats (Interval dp problem)

        # normalise the cuts array 
        cuts = [0] + sorted(cuts) + [n]

        @lru_cache(None)
        def dp(i,j): # min cost to cut stick starting at cuts[i] and ending at cuts[j]
            if j - i == 1: # cannot cut between length of 1
                return 0

            min_cost = float('inf')
            for k in range(i+1, j):
                # Cost = Length of current stick + cost of left side + cost of right side
                current_cost = (cuts[j] - cuts[i]) + dp(i,k) + dp(k,j)
                min_cost = min(min_cost, current_cost)

            return min_cost
        m = len(cuts)
        # solve for full stick
        return dp(0, m-1)
        