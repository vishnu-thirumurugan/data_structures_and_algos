class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_xors = [0]*(n+1)

        for i in range(n):
            prefix_xors[i+1] = prefix_xors[i] ^ arr[i]


        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                for k in range(j,n):
                    xor1 = prefix_xors[j-1+1] ^ prefix_xors[i]
                    xor2 = prefix_xors[k+1] ^ prefix_xors[j]

                    if xor1 == xor2:
                        res += 1

        return res

        