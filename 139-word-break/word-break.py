class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) # for order of 1 search
        n = len(s)

        @lru_cache
        def dfs(pos):
            if pos == n: # all words found in dict
                return True

            for j in range(pos+1, n+1):
                if s[pos:j] in wordSet and dfs(j):
                    return True
            # if no word found
            return False

        return dfs(0)

            

        