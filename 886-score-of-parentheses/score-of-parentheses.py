class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # stack --> o(n) run time, o(n) space
        stack = []
        finalScore = 0

        for ch in s:
            if ch == '(':
                stack.append(0)  # appending local score
            else:
                val = stack.pop()
                score = max(2*val,1)
                
                if stack:
                    stack[-1] += score
                else:
                    finalScore += score

        return finalScore
        