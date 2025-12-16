class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # bfs with value based teleport (previous soln --> dfs)
        n = len(arr)

        q = deque([start])
        visited = set([start])  

        while q:
            idx = q.popleft()

            if arr[idx] == 0: # reached goal
                return True

            forward_jump = idx+arr[idx]
            backward_jump = idx-arr[idx]

            if forward_jump < n and forward_jump not in visited : # out of bounds 1 
                q.append(forward_jump)

            if backward_jump >= 0 and backward_jump not in visited: # out of bounds 2
                q.append(backward_jump)

            visited.add(idx)

        return False



            




            
        