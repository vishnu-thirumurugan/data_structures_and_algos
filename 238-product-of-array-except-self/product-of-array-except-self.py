class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solving using division is also tricky
        product = 1
        for i in nums:
            product = product * i

        zero_less_product = 1
        if nums.count(0) > 1: # if u have multiple zeros, its any way zero
            zero_less_product = 0
        else:
            for i in nums:
                if i != 0:
                    zero_less_product = zero_less_product * i

        

        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[i] = product//nums[i]
            else:
                nums[i] = zero_less_product

        return nums


        