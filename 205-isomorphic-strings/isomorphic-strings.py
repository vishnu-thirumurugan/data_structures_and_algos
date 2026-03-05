class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}

        for i in range(len(s)):
            if s[i] in hashMap:
                if hashMap[s[i]] != t[i]:
                    return False
            else:
                hashMap[s[i]] = t[i]

        hashMap2 = {}
        for i in range(len(s)):
            if t[i] in hashMap2:
                if hashMap2[t[i]] != s[i]:
                    return False
            else:
                hashMap2[t[i]] = s[i]

        return True
        