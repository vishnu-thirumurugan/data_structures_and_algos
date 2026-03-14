class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # avoid while loop method
        n = len(s)
        last_seen = {}
        left = 0
        longest = 0

        for right, c in enumerate(s):

            if c in last_seen and last_seen[c] >= left:
                left = last_seen[s[right]] + 1

            last_seen[s[right]] = right
            longest = max(longest, right - left + 1)
            
        return longest

            