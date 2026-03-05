class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # to remove duplicates from index i 
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # avoid duplicates coming from the left
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # avoid duplicates coming from the right
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                # if sum > 0, reduce right
                elif s > 0:
                    right -= 1
                # if sum < 0, need more for contribution --> increase left 
                else:
                    left += 1
                
        return result

            

            

            
            