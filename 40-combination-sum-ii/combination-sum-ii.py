class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 0/1 knpsack 

        n = len(candidates)
        res = []
        candidates.sort() # sorting to avoid duplicates

        def backtrack(start, path, curr_target):
            if curr_target == 0:
                res.append(path[:])
                return

            # n branches in the begining
            for i in range(start, n):
                # avoid duplicates at same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue # to next branch

                if curr_target < 0:
                    break

                backtrack(i+1, path+[candidates[i]], curr_target - candidates[i])

        backtrack(0,[],target)
        return res


        

        