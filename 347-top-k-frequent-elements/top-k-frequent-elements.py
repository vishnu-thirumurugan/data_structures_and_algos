from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter way 
        freq = Counter(nums)
        res = []
        top_k = freq.most_common(k)
        for key,_ in top_k:
            res.append(key)
        return res
            


        