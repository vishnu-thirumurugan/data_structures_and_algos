class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        flag = 0
        for i in range(m-n+1):
            left = i
            for j in range(n):
                if haystack[left] == needle[j]:
                    flag = 1
                    left +=1

                else:
                    flag = 0
                    break

            if flag:
                return i

        return -1
            


        

