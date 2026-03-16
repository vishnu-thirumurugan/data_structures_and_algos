class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = []
        stack = []

        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            res.append(stack[-1]-i if stack else 0)
            stack.append(i)
        return res[::-1]



            
        