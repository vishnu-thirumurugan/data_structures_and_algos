class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        last_seen = {}
        longest = 0

        for right in range(n):
            c = s[right]
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
            last_seen[c] = right
            longest = max(longest, right - left + 1)

        return longest


            