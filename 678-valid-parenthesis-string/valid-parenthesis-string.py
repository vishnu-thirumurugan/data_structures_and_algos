class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = 0  # max number of left open brackets we can have
        leftMin = 0  # min number of left open brackets we can have

        for ch in s:
            if ch =='(':
                leftMax += 1
                leftMin += 1
            elif ch == ')':
                leftMax -= 1
                leftMin -= 1

            else: # * character
                leftMax += 1
                leftMin -= 1
            
            if leftMax < 0:
                # ))((
                return False
            
            leftMin = max(leftMin,0)

        return leftMin == 0
        