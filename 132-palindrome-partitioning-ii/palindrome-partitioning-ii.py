class Solution:
    def minCut(self, s: str) -> int:
        # dp + expand around centre solution
        # O(n^2) time, O(n) memory
        n = len(s)
        # number of cuts needed till index i
        # initialize to worst case

        dp_min_cuts = list(range(n)) # min cut req in worst case from 0 to i

        for i in range(n):
            # odd length palindromes
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                # dp part
                new_cut = 0 if left == 0 else dp_min_cuts[left-1] + 1  # min cuts till l - 1 plus this palindrome
                dp_min_cuts[right] = min(dp_min_cuts[right], new_cut) # update the current right index
                left -= 1
                right += 1

            # even length palindromes
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                new_cut = 0 if left == 0 else dp_min_cuts[left-1] + 1  # min cuts till l - 1 plus this palindrome
                dp_min_cuts[right] = min(dp_min_cuts[right], new_cut) # update the current right index
                left -= 1
                right += 1

        return dp_min_cuts[-1] # for full string, what is min cut