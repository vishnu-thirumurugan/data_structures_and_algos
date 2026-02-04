class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n-m+1):
            left = i
            for j in range(m):
                if haystack[left] == needle[j]:
                    flag = 1
                    left+= 1
                else:
                    flag = 0
                    break

            if flag:
                return i
             
        return -1

        

