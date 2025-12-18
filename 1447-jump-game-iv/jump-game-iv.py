class Solution:
    def minJumps(self, arr: List[int]) -> int:

        # each index --> node
        # each jump --> edge
        # all edges have equal weight
        # unweighted shortest path --> BFS -->o(n), o(n) time and space

        
        n = len(arr)

        if n == 1: # edge case
            return 0

        # same_value_indexes
        same_value_indices = defaultdict(list)
        for i, v in enumerate(arr): # index, value
            same_value_indices[v].append(i)

        visited = [False] * n

        q = deque([(0, 0)]) # pass index, steps
        visited[0] = True

        while q:
            index, steps = q.popleft()

            if index == n - 1:
                return steps

            if index + 1 < n and not visited[index+1]:
                visited[index+1] = True
                q.append((index+1, steps+1))

            if index - 1 >= 0 and not visited[index-1]:
                visited[index-1] = True
                q.append((index-1, steps+1))

            # visited j 
            for indices in same_value_indices[arr[index]]:
                if visited[indices] == False:
                    visited[indices] = True
                    q.append((indices, steps+1))

            # pruning
            same_value_indices[arr[index]].clear()  # else worst case = o(n2)

        return -1
        