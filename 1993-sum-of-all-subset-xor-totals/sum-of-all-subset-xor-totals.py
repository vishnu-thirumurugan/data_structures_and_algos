class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # bit manipulation with o(n) --> aryan mittal channel
        OR = 0
        n = len(nums)
        for num in nums:
            OR |= num
        # each number appears in half of the subsets
        # there are 2**n number of subsets
        # OR sets bit if atleast one of the bits is set
        return OR * (1<<(n -1))