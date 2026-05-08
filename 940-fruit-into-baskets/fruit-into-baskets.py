class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c = defaultdict(int)
        left = 0
        n = len(fruits)
        remaining = 2 # to put into baskets

        res = 0

        for right in range(n):
            fruitCat = fruits[right]
            if c[fruitCat] == 0: # new fruit addded
                remaining -= 1
            c[fruitCat] += 1

            while remaining < 0: # when there are more than 2 in baskets
                removeFruit = fruits[left]
                c[removeFruit] -= 1
                if c[removeFruit] == 0: # one category completely removed
                    remaining += 1

                left += 1

            res = max(res, right-left + 1)

        return res

            

        