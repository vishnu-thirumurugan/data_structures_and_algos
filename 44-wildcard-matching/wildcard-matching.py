class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n, m = len(s), len(p)

        # Using a dictionary or @cache for memoization
        memo = {}

        def dp(i, j):
            # 1. Check Base Cases
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Both exhausted -> Match
            if j == m:
                return i == n
            
            # String exhausted -> Only True if remaining pattern is all '*'
            if i == n:
                # Check if all remaining chars in p are '*'
                return all(x == '*' for x in p[j:])

            # 2. Transitions
            if p[j] == s[i] or p[j] == '?':
                res = dp(i + 1, j + 1)
            elif p[j] == '*':
                
                k = j
                while k < m and p[k] == '*':
                    k += 1
                # Option 1: Treat '*' as empty (skip pattern index)
                # Option 2: Treat '*' as consuming s[i] (skip string index)

                res = dp(i, k) or dp(i + 1, k-1)
            else:
                res = False
            
            memo[(i, j)] = res
            return res

        return dp(0, 0)