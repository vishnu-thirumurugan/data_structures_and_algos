class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        st = ''
        for ch in s:
            if ch in st:
                print(st)
                st = ch
                count += 1  
            else:
                st += ch

        return count + 1