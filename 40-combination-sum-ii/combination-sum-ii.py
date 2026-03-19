class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def backtrack(start, path, currSum):
            if currSum == 0:
                res.append(path.copy())
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if currSum < 0:
                    break

                backtrack(i+1, path+[candidates[i]], currSum - candidates[i])

        backtrack(0,[],target)
        return res

            



        

        