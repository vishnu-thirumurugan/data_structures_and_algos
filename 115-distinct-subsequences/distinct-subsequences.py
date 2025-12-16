class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]=number of ways to form t[0..j−1] from s[0..i−1]

        m, n = len(s), len(t)

        @lru_cache(None)
        def dp(i, j):
            if j >= n: # t is achieved
                return 1
            
            if i >= m: # t is not achieved, s is exhausted, cannot form
                return 0

            if s[i] == t[j]: 
                # you have two choices, take this or leave this s[i]
                # dp(i+1, j+1) --> consider s[i] and t[j] match
                # dp(i+1,j) --> I am looking for ch in latter appearances
                return dp(i+1, j+1) + dp(i+1, j) 
            
            else: #s[i] != t[j]
                return dp(i+1, j)

        return dp(0,0)


            


        