from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        new_dict = sorted(freq.items(), key = lambda x: x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(new_dict[i][0])
        return res
            


        