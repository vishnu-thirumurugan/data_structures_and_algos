class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # not O(1)
        freq = Counter(nums)
        return max(freq, key = freq.get)
        