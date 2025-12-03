class Solution:
    def minDistance(self, s1: str, s2: str) -> int:

        # check notes --> gemini + ipad
        m, n = len(s1), len(s2)

        memo = {}

        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i == m: # s1 empty --> add remaining from s2
                return n - j

            if j == n: # s2 empty --> delete remaining from s1
                return m - i

            # if both are same
            if s1[i] == s2[j]: # they are matching skip to next
                memo[(i,j)] = helper(i+1, j+1) # no extra operation, just move forward
            
            # if they are not same, take minimum of 3 decission branch
            else:
                delete_op = helper(i+1,j) # delete one from s1
                insert_op = helper(i, j+1) # insert char from s2 into s1
                replace_op = helper(i+1, j+1) # replaced --> match --> move forward in both 
                memo[(i,j)] = 1 + min(insert_op, delete_op, replace_op) # 1 coz you do any of the three

            return memo[(i,j)]

        return helper(0,0)




        