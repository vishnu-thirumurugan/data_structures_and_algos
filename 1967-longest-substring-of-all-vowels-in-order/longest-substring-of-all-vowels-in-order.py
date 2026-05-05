class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        maxLen = 0
        currLen = 1
        uniqueCount = 1

        for i in range(1,len(word)):
            if  word[i] == word[i-1]:
                # keep going
                currLen += 1

            elif word[i] > word[i-1]:
                # new vowel in order
                currLen += 1
                uniqueCount += 1

            else:
                # reset
                currLen = 1
                uniqueCount = 1

            if uniqueCount == 5:
                maxLen = max(maxLen, currLen)

        return maxLen