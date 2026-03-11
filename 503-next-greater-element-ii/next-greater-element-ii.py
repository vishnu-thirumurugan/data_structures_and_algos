class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1]*n

        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()

            if stack and i < n:
                res[i] = stack[-1] if stack else -1

            stack.append(nums[i%n])

        return res