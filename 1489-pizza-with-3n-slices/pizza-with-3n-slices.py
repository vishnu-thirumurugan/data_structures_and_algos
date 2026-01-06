class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        # circular dp 
        # simialar to house robber 2 

        # change --> u can pick only n --> this becomes one of the states
        n = len(slices)
        
        def solve(arr):
            @lru_cache(None)
            def dp(idx, pick):
                if pick == n//3:
                    return 0
                # u took less than n // 3
                if idx >= n - 1:
                    return -math.inf

                # skip
                skip = dp(idx+1, pick)
                #take
                take = arr[idx] + dp(idx+2, pick+1)

                return max(skip, take)

            return dp(0,0)

        return max(solve(slices[:-1]), solve(slices[1:]))



            


            
            
        