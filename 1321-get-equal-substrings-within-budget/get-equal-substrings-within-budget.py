class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currCost = 0
        left = 0
        maxLen = 0
        currLen = 0

        for right in range(len(s)):
            while currCost > maxCost:
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1


            currCost += abs(ord(t[right]) - ord(s[right]))
            
            if currCost <= maxCost:
                maxLen = max(maxLen, right-left+1)

        return maxLen

            

        