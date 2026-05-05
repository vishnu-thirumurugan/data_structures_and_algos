class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = nums[0]
        maxProd = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]
            if num < 0:
                # swap --> multipying with negative number changes the game
                minProd, maxProd = maxProd, minProd
            
            minProd = min(minProd*num, num)
            maxProd = max(maxProd*num, num)
            res = max(res, maxProd)

        return res

            