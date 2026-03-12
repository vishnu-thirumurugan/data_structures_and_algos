import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heapq way
        c = Counter(nums)
        top_k = heapq.nlargest(k, c.items(), key = lambda x:x[1])
        res = []
        for i in range(k):
            res.append(top_k[i][0])
        return res

            


        