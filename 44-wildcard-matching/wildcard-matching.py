class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_p = []
        for x in p:
            if new_p == []:
                new_p.append(x)
            elif x == "*" and new_p[-1]== "*":
                continue
            else:
                new_p.append(x)

        p = ''.join(new_p)

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
                # Option 1: Treat '*' as empty (skip pattern index)
                # Option 2: Treat '*' as consuming s[i] (skip string index)
                res = dp(i, j + 1) or dp(i + 1, j)
            else:
                res = False
            
            memo[(i, j)] = res
            return res

        return dp(0, 0)