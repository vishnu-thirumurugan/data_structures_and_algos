class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [0]*n
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i

            stack.append(i)

        return res

            
        