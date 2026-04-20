class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = defaultdict(int)
        banned_set = set(banned)
        clean_paragraph = re.sub(r'[^\w\s]', ' ', paragraph)

        for word in clean_paragraph.split():
            word = word.strip()
            if word.lower() not in banned_set:
                words[word.lower()] += 1
        # print(words)
        answer = sorted(words.items(), key = lambda x:x[1], reverse = True)
        # print(answer)
        return answer[0][0]
        