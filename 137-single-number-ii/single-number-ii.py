class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0 # if the number appeared ones (3k+1)
        twos = 0 # if the number appeared twice (3k+2) 
        # if it appears thrice (3k+3), i dont need to keep track -> it wont be ans

        for x in nums:
            ones = (ones ^ x) & ~twos # include the number if its not in twos (only first appearance, not third)
            twos = (twos ^ x) & ~ones # include only second appeance + remove thrid appearance

        # as everything is happening bitwise, on a whole you will get answer
        return ones



            

            