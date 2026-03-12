import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # intuition - break the loop after k 
        c = Counter(nums)
        sorted_list = sorted(c.items(), key = lambda x:x[1], reverse = True)
        res = []
        for key, val in sorted_list:
            if k == 0:
                break
            k-=1
            res.append(key)
        return res

            


        