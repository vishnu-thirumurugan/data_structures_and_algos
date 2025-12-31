class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def backtrack(idx, path):
            if idx == n: # reached last idx
                res.append(path[:])
                return

            # either u take and explore or leave and explore

            # take and explore
            backtrack(idx+1, path + [nums[idx]])
            # leave and explore
            backtrack(idx+1, path)

        res = []
        backtrack(0,[])

        return res
            
                
