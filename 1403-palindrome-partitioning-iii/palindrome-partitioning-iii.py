class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # this is Partition DP
        # solve 647 and 132 before this. 132 must

        # intuition - cost of transformation 
        ###########
        # I might need a helper tool. given a string s [i...j], 
        # the helper should say how many changes are needed to obtain palindrome
        # call this as cost(i,j)
        # precalculate and store it for later use
        
        # intuition - dp states:
        ############
        # i --> index where current prefix ends
        # c --> number of partitions made so far
        # dp[c][i] --> min changes required to split s[0....i] into c pal groups 
        

        # intuition - state transition
        ###########
        # to calculate dp[c][i] --> make last cut at every possible 'j'
        # such that s[0...j] we have c-1 cuts and j+1 to i will be 1 palindrome
        n = len(s)
        # 1. Precompute costs for all substrings
        cost = [[0]*n for _ in range(n)]
        for length in range(2,n+1):
            for i in range(n-length+1):
                j = i + length -1
                # If chars match, cost is same as inner part. If not, inner part + 1
                cost[i][j] = cost[i+1][j-1] + (1 if s[i]!=s[j] else 0)

        # 2. DP table 
        # dp[c][i] = min changes for s[0...i] using c partitions
        # Initialize with infinity
        dp = [[float('inf')]*n for _ in range(k+1)]

        # 3. Base case 1; partition
        for i in range(n):
            dp[1][i] = cost[0][i]

        # 4. Fill entire table
        for c in range(2, k+1): # for each partition count
            for i in range(c-1, n): # for each end index i
                # try cutting at every j  
                for j in range(c-2, i):
                    # Current Cost = Cost of c-1 partitions ending at j 
                    #              + Cost of turning s[j+1...i] into palindrome
                    dp[c][i] = min(dp[c][i],dp[c-1][j] + cost[j+1][i])

        return dp[k][n-1]