class Solution:
    def countArrangement(self, n: int) -> int:
        used = [0]*(n+1)

        def dfs(pos):
            # all the numbers are visited and used
            if pos > n:
                return 1
            
            count = 0
            for num in range(1,n+1): # use all the numbers in this range
                if used[num] == 0 and (num % pos == 0 or pos%num == 0):
                    used[num] = 1
                    count += dfs(pos + 1)
                    used[num] = 0

            return count

        return dfs(1)
            

        