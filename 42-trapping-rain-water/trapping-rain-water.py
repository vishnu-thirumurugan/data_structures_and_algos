class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        lmax = [height[0]]*n
        rmax = [height[-1]]*n

        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i])
        
        for i in range(n-2,-1,-1):
            rmax[i] = max(rmax[i+1], height[i])

        
        res = 0
        for i in range(1, n-1):
            res += min(lmax[i],rmax[i]) - height[i]

        return res
