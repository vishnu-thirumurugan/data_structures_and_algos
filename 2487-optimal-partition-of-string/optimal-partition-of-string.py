class Solution:
    def partitionString(self, s: str) -> int:
        # bit manipulation > array > set for same o(n)
        flag = 0
        count = 1 # string length constraint --> atleast one string will be present


        for i in s:
            val = ord(i)-ord('a')
            if flag & (1<<val): # the element is already present
                count += 1   # create new sub-string
                flag = 0   # reset flag for next cycle
            
            flag = flag | (1<<val) # if not present keep track / first element of sub-string
    
        return count




