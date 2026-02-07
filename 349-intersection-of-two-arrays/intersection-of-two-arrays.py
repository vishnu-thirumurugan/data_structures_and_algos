class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        
        for num in nums1:
            d[num] += 1

        output = set()
        for num in nums2:
            if d[num] > 0:
                output.add(num)

        return list(output)

        
        