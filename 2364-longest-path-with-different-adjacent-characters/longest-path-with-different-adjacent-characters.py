class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # N - ary tree
        # u need adjaceny list (or parent child connections)
        n = len(parent)

        adj_list = defaultdict(list)
        for ch, pr in enumerate(parent):
            adj_list[pr].append(ch)

        # print(adj_list)
        self.ans = 0
        def dfs(root):
            top_1, top_2 =  0,0
            for ch in adj_list[root]:
                if s[root] != s[ch]:
                    temp = dfs(ch)
                    if temp >= top_1:
                        top_1, top_2 = temp, top_1
                    elif temp > top_2:
                        top_2 = temp

                else:
                    dfs(ch)

            self.ans = max(self.ans, top_1 + top_2 + 1)

            return 1 + top_1


            
        dfs(0)
        return self.ans
        








        