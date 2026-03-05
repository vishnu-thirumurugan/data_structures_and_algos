class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # this is the optimal way of solving
        # sliding window + hashmap
        m = len(s)
        n = len(p)

        if n > m:
            return []

        sCount = [0]*26
        pCount = [0]*26

        res = []

        # build a window
        for i in range(n):
            sCount[ord(s[i]) - ord('a')] += 1
            pCount[ord(p[i]) - ord('a')] += 1
        
        if sCount == pCount:
            res.append(0)

        # slide the window
        for i in range(n,m):
            sCount[ord(s[i]) - ord('a')] += 1
            sCount[ord(s[i-n])- ord('a')] -= 1

            if sCount == pCount:
                res.append(i-n+1)

        return res
