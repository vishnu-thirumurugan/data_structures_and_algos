class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def backtrack(start, path, curr_target):
            if curr_target == 0:
                res.append(path.copy())
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if curr_target < 0:
                    return

                backtrack(i+1, path+[candidates[i]], curr_target-candidates[i])

        backtrack(0,[],target)
        return res 
            



        

        