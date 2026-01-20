class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # nums.sort()
        
        left, right= 1, n-1

        while left < right:
            count = 0
            mid = (left+right)//2
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                # ans = mid
                right = mid
            else:
                # ans = mid
                left = mid + 1

        return left


        