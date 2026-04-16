class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
        
        if stack:
            ans += len(stack)

        return ans
        