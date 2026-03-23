class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = math.inf
        nums.sort()

        for i in range(n):
            
            left = i+1
            right = n-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == target:
                    return target
                elif s > target:
                    right -= 1
                else:
                    left += 1

                if abs(s - target) < abs(ans-target):
                    ans = s

        return ans

