class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        memo = {}

        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            # base case:
            if i == m or j == n: # empty string
                return 0 

            # current indices match --> tracking suffixes
            if s1[i] == s2[j]:
                res = 1 + helper(i+1, j+1)

            else:
                # no match -> explore both branch
                res = max(helper(i+1,j), helper(i, j+1))

            memo[(i,j)] = res

            return memo[(i,j)]

        return helper(0,0)

