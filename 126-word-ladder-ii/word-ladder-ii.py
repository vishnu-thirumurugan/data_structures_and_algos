class Solution:
    def findLadders(self, begin: str, end: str, word_list: List[str]) -> List[List[str]]:
        # two phases
        #1. bfs and find the parents and the shortest transformation length
        #2. do dfs on parents and find all the path

        # distance[word] = shortest distance from beginWord
        # parents[word] = list of words that can reach `word` in shortest way

        word_list = set(word_list) # o(1) look up and avoid repitition

        # edge case
        if end not in word_list:
            return []

        found = False # for endword

        q = deque([begin])
        level = 0

        parents = defaultdict(list) # built during BFS and used to find all paths in DFS
        distance = {begin:0} # to build DAG using BFS

        while q and not found:

            level += 1
            for _ in range(len(q)): # pop by levels --> so that you can delete words after level (to avoid repetition)
                word = q.popleft()
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == word[i]: # dont form same word
                            continue
                        
                        next_word = word[:i] + ch + word[i+1:]

                        if next_word not in word_list:
                            continue

                        if next_word not in distance:
                            distance[next_word] = level
                            parents[next_word].append(word)
                            if next_word == end:
                                found = True
                            q.append(next_word)

                        elif distance[next_word] == level:
                            parents[next_word].append(word)

                        else:
                            pass # I dont want longer answers

            # remove the words AFTER A LEVEL to avoid forming same word again
            for w in distance.keys():
                word_list.discard(w)
        
        res = []

        def dfs(word, path):
            if word == begin:
                res.append(path[::-1]) # reverse the path and return
                return

            for p in parents[word]:
                dfs(p, path + [p])

        dfs(end, [end])
        return res


        


                        



                        

            



        