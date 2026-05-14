class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = 0 
        ans = 0
        count = {'a':0, 'b':0, 'c':0}

        for right in range(n):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0: # shrink left
                count[s[left]] -= 1
                left += 1
                ans += n-right

        return ans
        