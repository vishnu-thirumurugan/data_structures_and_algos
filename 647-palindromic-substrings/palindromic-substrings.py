class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            left, right = i,i
            while left >=0 and right <= n-1:
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break

            left, right = i, i+1
            while left >= 0 and right <= n-1:
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break

        return res
