import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most_common() function way
        c = Counter(nums)
        top_k = sorted(c.items(), key = itemgetter(1), reverse = True)
        res = []
        for i in range(k):
            res.append(top_k[i][0])
        return res

            


        