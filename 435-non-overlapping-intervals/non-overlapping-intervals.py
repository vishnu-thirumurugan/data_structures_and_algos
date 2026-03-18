class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        res = 0
        n = len(intervals)
        end = - math.inf

        for start, finish in intervals:
            if start >= end:
                end = finish
                res += 1
        
        return n - res


