class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        c = Counter(nums)

        res = []

        def backtrack(nums, path):
            if len(path) == n:
                res.append(path.copy())
                return

            for num in c:
                if c[num] > 0: # then only you can use it
                    c[num] -= 1
                    path.append(num)
                    backtrack(nums, path)
                    path.pop()
                    c[num] += 1

        backtrack(nums,[])
        return res
