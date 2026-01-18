class Solution:
    def partitionString(self, s: str) -> int:
        # bit manipulation > array > set for same o(n)
        n = len(s)
        flag = 0
        count = 1 # string length constraint --> atleast one string will be present

        i = 0  # index to move on string
        while i < n:
            val = ord(s[i])-ord('a')
            # print(val)
            if flag & (1<<val): # the element is already present
                count += 1   # create new sub-string
                flag = 0   # reset flag for next cycle
            
            flag = flag | (1<<val) # if not present keep track / first element of sub-string
            # print(flag)
            i+= 1

        return count




