class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSumCount = {0:1}

        currPrefSum = 0
        ans = 0

        for num in nums:
            currPrefSum += num

            # if x-k in dict, you found a subarray with k
            if currPrefSum - k in prefSumCount:
                ans += prefSumCount[currPrefSum-k]

            prefSumCount[currPrefSum] = prefSumCount.get(currPrefSum,0) + 1

        return ans
        
        