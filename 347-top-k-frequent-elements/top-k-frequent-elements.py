import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most_common() function way
        c = Counter(nums)
        top_k = c.most_common(k)
        res = []
        for key,_ in top_k:
            res.append(key)
        return res

            


        