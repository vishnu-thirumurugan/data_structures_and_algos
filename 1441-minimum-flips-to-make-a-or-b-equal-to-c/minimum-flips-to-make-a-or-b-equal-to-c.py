class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        # pure bit manipulation way 

        flips = 0 

        while a > 0 or b > 0 or c > 0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if cbit == 1:
                # any one bit should be 1 
                if abit | bbit == 0:
                    flips += 1

            else: # cbit = 0
                flips += abit + bbit

            # go to the next bits
            a= a>>1
            b = b>>1
            c = c>>1

        return flips
                        


            
        