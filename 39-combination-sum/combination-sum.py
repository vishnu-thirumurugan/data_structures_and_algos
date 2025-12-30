class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        # unbounded pick or not pick
        def backtrack(idx, path, curr_target):
            if idx == n and curr_target == 0:
                res.append(path.copy())

            if curr_target < 0 or idx >= n:
                return

            # pick
            path.append(candidates[idx])
            backtrack(idx, path, curr_target - candidates[idx]) # unbounded --> idx stays
            # not pick
            path.remove(candidates[idx])
            backtrack(idx + 1, path, curr_target)

        backtrack(0,[],target)
        return res

            
        
            
        