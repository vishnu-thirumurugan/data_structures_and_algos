class Solution:
    # this question is trivial when u solve leetcodequestion - Edit Distance
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @lru_cache(None)
        def helper(i,j):
            # if i exhausted --> delete the remaining in s2
            if i == m:
                return n - j

            # if j exhausted --> delete the remaining in s1
            if j == n:
                return m - i

            if s1[i] == s2[j]:
                return helper(i+1, j+1) # move ahead when match (no op)

            else:
                return 1 + min(helper(i+1,j), helper(i, j+1))

        return helper(0,0)


        