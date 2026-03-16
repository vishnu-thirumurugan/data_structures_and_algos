class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        currSum = 0 
        res = 0

        for num in nums:
            currSum += num

            if currSum - k in d:
                res += d[currSum-k]
            
            d[currSum] = d.get(currSum,0) + 1
        
        return res
        