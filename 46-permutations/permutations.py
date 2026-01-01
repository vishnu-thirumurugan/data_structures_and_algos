class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        boolean_map = [False]*n
        res = []

        def backtrack(path, boolean_map):
            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(n):
                print(boolean_map)
                if boolean_map[i] == False:
                    path.append(nums[i])
                    boolean_map[i] = True
                    backtrack(path, boolean_map)
                    path.pop()
                    boolean_map[i] = False

        backtrack([],boolean_map)
        return res

            
        