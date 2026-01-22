class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        pref_xors = [0 for _ in range(n+1)]


        for i in range(n):
            pref_xors[i+1] = pref_xors[i] ^ arr[i]

        # if two values are equal their xor will be zero
        # find i and k such that xor range is 0 
        # add count of all possible values of j from i to k 
        res = 0
        for i in range(n-1):
            for k in range(i+1, n):
                if pref_xors[k+1] - pref_xors[i] == 0:
                    # xors of (i to j - 1) and (j to k) are equal for all values of j
                    res += k - i

        return res


        

        