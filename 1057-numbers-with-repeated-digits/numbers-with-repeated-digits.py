class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # can be solved with combinatrics
        # solving by digit dp method
        # 4 states
        # current digit, is_less, is_started, mask
        # is_started --> used for filling leading zeros
        # is_less --> (if n = 543, i cant use  > 5 for first digit) --> keep tight
        # 0 to 4 at first digit--> is less --> i can use 0 to 9 at 2nd digit
        # if 5 at first digit --> not is less --> i need to use <= 4 at 2nd digit
        s = str(n)
        l = len(s)

        # returns number of unique digits
        @lru_cache(None)
        def digits_dp(idx, is_less, is_started, mask):
            if idx == l:
                return 1 if is_started else 0 # atleast one non zero digit in recursion
            
            limit = int(s[idx]) if not is_less else 9 # else u can fill from 0 to 9
            res = 0
            for d in range(limit+1):
                new_is_less = is_less or d < limit  # once is_less, for entire cycle, its is_less
                new_is_started = is_started or d > 0 # once started, its always started

                if not new_is_started: # put a leading zero and go to next digit
                    res += digits_dp(idx+1, True, False, 0) # no digits used, so mask --> 0

                else:
                    if not mask & (1 << d):
                        # if this digit is not used, you can use it
                        res += digits_dp(idx+1, new_is_less, new_is_started, mask | (1 << d))

            return res
        
        unique_digits = digits_dp(0, False, False, 0)
        return n - unique_digits


            


