class Solution:
    def countAndSay(self, n: int) -> str:
        # without while loop
        s = '1'
        # do repeatedly until u get to n
        for _ in range(n-1):
            res = ''
            count = 1
            # traverse until the string length
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    res += str(count)
                    res += s[i-1]
                    count = 1
            # print(s)
            res += str(count)
            res += s[-1]
            s = res
            # print(s)
        return s
        


            
            

        