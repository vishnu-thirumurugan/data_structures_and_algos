class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window appproach
        left = 0
        ans = 0
        char = set()

        for right in range(len(s)):
            # sliding windoe
            while s[right] in char:
                char.remove(s[left])
                left += 1

            # now the string has unique characters
            char.add(s[right])
            ans = max(ans, right-left+1)

        return ans

        