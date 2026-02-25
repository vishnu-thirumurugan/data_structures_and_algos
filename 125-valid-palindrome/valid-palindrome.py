class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for char in s:
            if char.isalpha():
                res += char.lower()
            elif char.isdigit():
                res += char
        left = 0 
        right = len(res)-1

        while left <= right:
            if res[left] != res[right]:
                return False
            left +=  1
            right -= 1

        return True
