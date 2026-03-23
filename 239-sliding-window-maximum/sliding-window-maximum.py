class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic deque
        q = deque()
        res = []

        for i in range(len(nums)):
            # current largest moving out of windows
            if q and q[0] <= i-k:
                q.popleft()

            # keep monotonic deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # once the window length has been reached
            if i >= k-1:
                res.append(nums[q[0]])

        return res



        
        