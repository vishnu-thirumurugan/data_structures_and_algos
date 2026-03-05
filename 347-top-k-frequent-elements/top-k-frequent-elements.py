import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap way 
        freq = Counter(nums)
        res = heapq.nlargest(k,freq.items(), key = lambda x:x[1])
        return [num[0] for num in res]

            


        