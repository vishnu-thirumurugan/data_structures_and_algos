class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            
            if start == n:
                return [''] # base case

            res = []

            for end in range(start+1, n+1):
                word = s[start:end]

                if word in wordSet:
                    subSentences = dfs(end)

                    for sentence in subSentences:
                        if sentence:
                            res.append(word+ ' ' + sentence) 
                        else:
                            res.append(word)

            memo[start] = res
            return res

        return dfs(0)                
        