class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        
        for i in range(m-n+1):
            j = i+n
            if haystack[i:j] == needle:
                return i

        return -1
            


        

