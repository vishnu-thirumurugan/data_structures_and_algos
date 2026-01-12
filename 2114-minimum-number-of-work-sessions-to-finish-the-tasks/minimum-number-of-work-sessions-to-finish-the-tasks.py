class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # bitmask dp --> dfs way --> subset bitmask dp
        # you need to know which tasks have already been completed
        # --> represented by masking
        # you also need to know how much time is left in the current session
        # sort to include the bigger elements first (pruning for recursion)
        tasks.sort(reverse = True)
        n = len(tasks)
        full_mask = (1<<n) - 1

        @lru_cache(None)
        def helper(mask, remaining):
            if mask == full_mask:  # all the tasks are done, no additional session needed
                return 0
            
            ans  = float('inf')

            for i in range(n): # explore all paths (this is where greedy failed)
                if not mask & (1<<i): # if task is not done
                    if tasks[i] <= remaining:
                        # you can do it (without satrting new session)
                        ans = min(ans, helper(mask|(1<<i), remaining - tasks[i] ))
                    else:
                        # start a new session and do it
                        ans = min(ans, 1+ helper(mask|(1<<i), sessionTime - tasks[i]))

            return ans

        return 1 + helper(0,sessionTime)


