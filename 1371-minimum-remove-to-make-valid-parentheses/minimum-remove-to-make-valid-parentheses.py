class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        res = []

        for i, ch in enumerate(s):
            if ch == '(':
                open_count += 1
                res.append(ch)

            elif ch == ')':
                if open_count > 0:
                    open_count -= 1
                    res.append(ch)
                else:
                    pass

            else:
                res.append(ch)

        
        for i in range(len(res)-1,-1,-1):
            if open_count == 0:
                break
            if res[i] == '(' and open_count > 0:
                del res[i]
                open_count -= 1

        return ''.join(res)





        