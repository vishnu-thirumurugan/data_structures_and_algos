class Solution:
    def longestPrefix(self, s: str) -> str:
        # this is based on kmp algorithm --> o(n)
        # lps[i] --> stores lenght of lps from index 0 to i
        n = len(s)
        lps = [0]*n
        j = 0
        for i in range(1, n): # lps[0] = 0 by default
            while j > 0 and s[i] != s[j]:
                j = lps[j-1]

            if s[i] == s[j]:
                j += 1

            lps[i] = j      
             
        return s[:lps[-1]]