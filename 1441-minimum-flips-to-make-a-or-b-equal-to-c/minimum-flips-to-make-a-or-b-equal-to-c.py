class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # bin conversion
        a = str(bin(a)[2:])
        b = str(bin(b)[2:])
        c = str(bin(c)[2:])
        a_len = len(a)
        b_len = len(b)
        c_len = len(c)

        n = max(a_len, b_len, c_len)
        if a_len < n:
            a = '0'*(n-len(a)) + a

        if b_len < n:
            b = '0'*(n-len(b)) + b

        if c_len < n:
            c = '0'*(n-len(c)) + c

        # print(a,b,c)

        count = 0
        for i in range(n):

            if c[i] == '1':
                if int(a[i]) | int(b[i]) != 1:
                    count += 1

            else: # bit is zero --> both should be zero
                if a[i] == b[i]: # they must be zero or 1
                    if a[i] == '1':# flip both bits
                        count += 2
                    # else: if 0, no flip needed
                else: # flip '1' to zero other is already zero
                    count += 1

            # print(count)

        return count
                        


            
        