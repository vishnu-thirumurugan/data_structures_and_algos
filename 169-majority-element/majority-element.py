class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        d_sorted = sorted(d.items(), key = lambda x : x[1], reverse = True)

        return   d_sorted[0][0]              
