class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # brute force - its exponential
        res = set()

        powers_x = [1]
        powers_y = [1]

        if x != 1:
            val = x
            while val < bound:
                powers_x.append(val)
                val *= x

        if y != 1:
            val = y
            while val < bound:
                powers_y.append(val)
                val *= y


        for px in powers_x:
            for py in powers_y:
                if px+py <= bound:
                    res.add(px+py)

        return list(res)