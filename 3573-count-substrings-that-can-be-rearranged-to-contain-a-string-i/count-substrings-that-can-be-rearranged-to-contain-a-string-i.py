class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # number of valid substring in [l....r] is n-r
        need = Counter(word2)
        window = Counter()

        required = len(need)
        formed = 0

        left = 0
        ans = 0
        n = len(word1)

        for right in range(n):
            ch = word1[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            # keep moving left 
            while formed == required:
                # update answer
                ans += n - right

                leftChar = word1[left]

                if leftChar in need and window[leftChar] == need[leftChar]:
                    formed -= 1
                    
                window[leftChar] -= 1
                left += 1
                

        return ans

        