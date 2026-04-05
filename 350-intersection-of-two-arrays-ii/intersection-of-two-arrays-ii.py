class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)

        for num in nums1:
            d[num] += 1

        output = []

        for num in nums2:
            if d[num] > 0:
                output.append(num)
                d[num] -= 1
        
        return output
        