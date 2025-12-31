class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # the pattern to avoid duplicate is sort and prune trees at same level
        n = len(nums)
        nums.sort()

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, n):
                if i > start and nums[i-1] == nums[i]: # prune tree to avoid duplicates
                    continue

                backtrack(i+1, path + [nums[i]])

        res = []
        backtrack(0,[])

        return res
        