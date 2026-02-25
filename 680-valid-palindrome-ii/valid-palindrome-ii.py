class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1 

        while left <= right:
            if s[left] != s[right]:
                if isPalindrome(left, right-1) or isPalindrome(left+1, right):
                    return True
                else:
                    return False

            left += 1
            right -= 1

        return True
