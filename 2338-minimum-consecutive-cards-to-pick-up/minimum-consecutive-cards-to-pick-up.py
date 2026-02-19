class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lastSeen = {}
        minLength = float('inf')

        for i in range(len(cards)):
            if cards[i] in lastSeen:
                minLength = min(minLength, i-lastSeen[cards[i]]+1)

            lastSeen[cards[i]] = i

        return - 1 if minLength  == float('inf') else minLength