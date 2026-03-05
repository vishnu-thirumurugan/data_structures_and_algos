class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # expand shrink sliding window problem
        # have, need concept 
        m = len(s)
        n = len(t)

        if not t: return ""

        tCount = Counter(t)
        window = {}

        result = [-1, -1]
        minLength = float('inf')
        have = 0
        need = len(tCount)

        l = 0
        for r in range(m):
            ch = s[r]
            window[ch] = window.get(ch,0) + 1

            if ch in tCount and window[ch] == tCount[ch]:
                have += 1
            
            while have == need:
                if (r-l+1) < minLength:
                    result = [l,r]
                    minLength = r-l+1

                window[s[l]] -= 1

                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1

                l += 1
        l,r = result
        # print(minLength)
        return s[l:r+1] if minLength != float('inf') else ""

        