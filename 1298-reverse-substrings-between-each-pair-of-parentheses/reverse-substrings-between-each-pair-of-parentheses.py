class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                # pop until you find  '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                # remove the '(' character
                stack.pop()

                # add the reversed characters
                stack.extend(temp)
            else:
                stack.append(ch)

        return ''.join(stack)
            
            

        