class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # optimal is order of n cube 
        # set i, j and traverse with left and right

        nums.sort() # sort to avoid duplicates from i 
        results = []
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                left = j+1
                right =  n-1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif s > target:
                        # reduce sum
                        right -= 1
                    else:
                        left += 1
                    

        return results
        