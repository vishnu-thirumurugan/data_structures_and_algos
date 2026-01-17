class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # brute force
        res = set()
        i = 0
        while x ** i < bound:
            j = 0 
            while x ** i + y ** j <= bound:
                res.add(x ** i + y ** j)
                if y == 1: # the values are going to remain same --> will never cross bound
                    break
                j += 1
            if  x == 1: # outer while will never cross bound
                break
            i += 1
        return list(res)