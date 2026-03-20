class Solution:
    def combinationSum3(self, n: int, target: int) -> List[List[int]]:
        res = []

        def backtrack(start, used, path, curr_sum):
            if used == n and curr_sum == target:
                res.append(path.copy())
                return

            
            for i in range(start, 10):

                if start > 9 or used > n or curr_sum > target:
                    return

                backtrack(i+1, used + 1,path + [i], curr_sum+i)

        backtrack(1,0,[],0)
        return res

            


        