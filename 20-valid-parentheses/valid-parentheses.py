class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ('(','{','['):
                stack.append(i)
            else: 
                if not stack:
                    return False
                if not ((stack[-1]=='(' and i ==')') 
                        or (stack[-1]=='{' and i =='}') 
                        or (stack[-1]=='[' and i ==']')):
                    return False
                
                stack.pop()

        if stack:
            return False
        return True