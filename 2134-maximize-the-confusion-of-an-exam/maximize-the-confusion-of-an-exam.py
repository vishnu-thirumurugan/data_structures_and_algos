class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        def helper(char):
            n = len(s)
            left= 0
            count = 0
            ans = 0

            for right in range(n):
                if s[right] != char:
                    count += 1 # change it
                while count > k:
                    if s[left] != char:
                        count -= 1
                    left += 1

                ans = max(ans, right-left+1)

            return ans

        return max(helper('T'), helper('F'))
        