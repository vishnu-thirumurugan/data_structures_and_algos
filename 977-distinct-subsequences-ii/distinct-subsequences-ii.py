class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        last = {}

        dp = [0]*(n+1)
        
        dp[0] = 1

        for i in range(1,n+1):
            ch = s[i-1]

            dp[i] = 2*dp[i-1]

            if ch in last:
                dp[i] = dp[i] - dp[last[ch] - 1] # remove duplicates

            last[ch] = i

        return (dp[n] - 1) % (10**9 + 7)

        