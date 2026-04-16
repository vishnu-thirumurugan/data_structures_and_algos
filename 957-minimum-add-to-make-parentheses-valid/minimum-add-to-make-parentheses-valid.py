class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        openCount = 0

        for ch in s:
            if ch == '(':
                openCount += 1
            else:
                if openCount:
                    openCount -= 1
                else:
                    ans += 1
        
        if openCount:
            ans += openCount

        return ans
        