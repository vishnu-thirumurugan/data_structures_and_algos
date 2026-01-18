class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        # st = ''
        partition_set = set()
        for ch in s:
            if ch in partition_set:
                # print(st)
                partition_set.clear()
                # st = ch
                partition_set.add(ch)
                count += 1
                

            else:
                # st += ch
                partition_set.add(ch)
                
        return count + 1