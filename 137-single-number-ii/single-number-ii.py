class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32): # 32 bit integer
            ibit_sum = 0 
            for num in nums:
                if (num >> i) & 1:
                    ibit_sum += 1
                    ibit_sum %= 3 # --> you get zero or 1 
            if ibit_sum != 0:
                ans |= (1 << i)

        if ans >= (1 << 31):
            ans -= (1 << 32)

        return ans

            

            