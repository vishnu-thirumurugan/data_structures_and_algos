class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(idx, path, currTarget):
            if idx == n and currTarget == 0:
                res.append(path.copy())
                return

            if currTarget < 0 or idx >= n :
                return

            path.append(candidates[idx])
            backtrack(idx, path, currTarget-candidates[idx])
            path.remove(candidates[idx])
            backtrack(idx+1,path, currTarget)

        backtrack(0, [], target)
        return res


            
        
            
        