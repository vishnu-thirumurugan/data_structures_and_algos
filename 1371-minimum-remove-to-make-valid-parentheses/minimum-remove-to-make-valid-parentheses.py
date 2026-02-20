class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0 
        res = []

        # first loop removes extra right bracket  --> ')'
        for i in range(len(s)):
            if s[i] == '(':
                open_count += 1
                res.append(s[i])
            elif s[i] == ')':
                if open_count > 0:
                    open_count -= 1
                    res.append(')')
                # else ignore this extra right bracket

            else: # if its a character --> append it 
                res.append(s[i])

        # second loop to avoid extra left bracket:
        n = len(res)
        final_res = []
        for i in range(n-1, -1, -1):
            if  open_count > 0 and res[i] == '(':
                open_count -= 1
            else:
                final_res.append(res[i])

        return ''.join(reversed(final_res))




        