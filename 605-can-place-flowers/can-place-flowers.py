class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        l = len(nums)
        if l == 1:
            if nums[0] == 1 and n == 0:
                return True
            elif nums[0] == 0 and n <= 1:
                return True
            else:
                return False

        count = 0
        for i in range(l):
            if i == 0:
                if not nums[i+1] and nums[i] == 0:
                    count += 1
                    nums[i] = 1

            elif i == l-1:
                if not nums[i-1] and nums[i] == 0:
                    count += 1
                    nums[i] = 1

            else:
                if not nums[i-1] and not nums[i+1] and nums[i] == 0:
                    count += 1
                    nums[i] = 1

            if count >=n:
                return True

        return False