class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(idx, path, curr_target):
            if idx == n and curr_target == 0:
                res.append(path.copy())
                return

            if idx >= n or curr_target < 0:
                return

            # pick
            path.append(candidates[idx])
            backtrack(idx,path, curr_target-candidates[idx]) # you can use the same element again
            path.remove(candidates[idx])
            backtrack(idx+1, path, curr_target)

        backtrack(0,[],target)
        return res

            
        
            
        