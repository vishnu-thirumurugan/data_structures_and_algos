class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # create such an array and see you will get an idea
        bin_form = bin(n-1)[2:]
        # print(bin_form)
    
        # fill these values of zeros at x from right to left
        res = []
        while x:
            if x & 1 == 0:
                if bin_form:
                    res.append(bin_form[-1])
                    bin_form = bin_form[:-1]
                else:
                    res.append('0')

            else:
                res.append('1')
            
            x >>= 1

        
        return int(bin_form + ''.join(reversed(res)),2)

        







        