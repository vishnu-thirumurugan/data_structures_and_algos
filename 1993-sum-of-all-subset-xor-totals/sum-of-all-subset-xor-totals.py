class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # bit manipulation way
        n = len(nums) 
        summ = 0
        # mask runs from 0 to pow (2, n) -1 
        for mask in range((1<<n)): #--> generates all the subset
            xor_total = 0
            # for each bit in the mask
            for i in range(n):
                if mask & (1<<i):            #(1<<i) checks i th bit is set or not
                    xor_total ^= nums[i]
            summ += xor_total
        return summ