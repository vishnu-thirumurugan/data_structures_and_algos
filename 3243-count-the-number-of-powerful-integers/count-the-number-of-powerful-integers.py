class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        l2 = len(s)
        def count(N):
            n_str = str(N)
            l1 = len(n_str)
            if l1 < l2:
                return 0
            @lru_cache(None)
            def digit_dp(idx, is_less): # is less --> tight
                if idx == l1 - l2:
                    # chek if all the digits or less than limit
                    suffix_possible = True
                    for char in s:
                        if int(char) > limit:
                            suffix_possible = False

                    if not suffix_possible:
                        return 0
                    # check the string s falls outside N
                    if not is_less:
                        if s >  n_str[idx:]:
                            return 0 

                    return 1

                res = 0
                # check for the upper limit --> limit tight
                upper = int(n_str[idx]) if not is_less else 9 # u can fill upto 9, if its not tight

                # decission branch --> all possibilities
                for d in range(min(upper, limit)+1):
                    res += digit_dp(idx+1, is_less or d < upper)

                return res

            return digit_dp(0,False)


        # count(high) --> possible numbers from 0 to finish
        # count(low-1) --> possible numbers from 0 to start - 1
        return count(finish) - count(start-1)
        