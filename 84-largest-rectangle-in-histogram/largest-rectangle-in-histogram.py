class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []
        left_small_index = [-1]*n
        right_small_index = [n]*n

        # left smallest
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left_small_index[i] = stack[-1]
            stack.append(i)

        stack = []
        # right smallest
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right_small_index[i] = stack[-1]
            stack.append(i)

        maxArea = -math.inf
        # print(left_small_index)
        # print(right_small_index)
        for i in range(n):
            length = right_small_index[i] - left_small_index[i] - 1
            currArea = length*nums[i]
            maxArea = max(maxArea,currArea)
        return maxArea



        