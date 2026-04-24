class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.strip().split(' ')
        words = [
            word.lower() if i == 0 else word.capitalize()
            for i, word in enumerate(words)
        ]

        return '#' + ''.join(words)[:99]
        