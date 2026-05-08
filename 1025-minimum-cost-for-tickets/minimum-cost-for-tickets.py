class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @lru_cache(None)
        def dp(idx, validDate):
            if idx == n:
                return 0

            if days[idx] <= validDate:
                # continue to next idx
                return dp(idx+1, validDate) # without buying pass

            return (
                min(
                    costs[0]+dp(idx+1, days[idx]),
                    costs[1]+dp(idx+1, days[idx]+6),
                    costs[2]+dp(idx+1, days[idx]+29)
                )
            )
        return dp(0,0)
        