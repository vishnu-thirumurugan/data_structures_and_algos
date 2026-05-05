class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        count = 0
        longestSr = 0

        for right in range(n):
            if right > 0 and s[right] == s[right-1]:
                count += 1
            while count > 1:
                left += 1
                if s[left] == s[left-1]:
                    count -= 1

            longestSr = max(longestSr, right-left +1)

        return longestSr if longestSr != 0 else 1

            



        