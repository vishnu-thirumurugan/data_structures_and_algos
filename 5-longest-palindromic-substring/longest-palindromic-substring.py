class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        n = len(s)
        if n==1:
            return s
        res = ""
        # expand around the centre
        for i in range(n):
            # odd length
            left, right = i,i
            while left >= 0 and right <= n-1:
                if s[left] == s[right]:
                    if right-left+1 > maxLength:
                        maxLength = right-left+1
                        res = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break

            left, right = i,i+1
            while left >= 0 and right <= n-1:
                if s[left] == s[right]:
                    if right-left+1 > maxLength:
                        maxLength = right-left+1
                        res = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break

        return res
        
        