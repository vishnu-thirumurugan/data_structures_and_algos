import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        top_k = sorted(c.items(), key = lambda x:x[1], reverse = True)
        res = []
        for key, val in top_k:
            if k == 0:
                break
            res.append(key)
            k-= 1
        return res
            


        