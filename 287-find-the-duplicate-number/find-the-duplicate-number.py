class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # nums.sort()
        
        left, right = 1, n
        
        while left <= right:
            count_left, count_right = 0, 0
            mid = (left+right)//2
            for i in nums:
                if i < mid:
                    count_left += 1
                elif i > mid:
                    count_right += 1

            if count_left + count_right not in (n, n-1):
                return mid

            elif count_left >= mid:
                ans = mid
                right = mid - 1
            else:
                ans = mid
                left = mid+1

        return ans


        