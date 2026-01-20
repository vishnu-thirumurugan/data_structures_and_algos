class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums) - 1
        duplicate = 0
        
        # Iterate through each bit position (0 to 31 for 32-bit integers)
        # Note: Since n is usually small on LeetCode, we can often stop at bit 17 or 20
        for bit in range(32):
            mask = (1 << bit)
            count_array = 0
            count_range = 0
            
            for i in range(n + 1):
                # Count bits in the actual array
                if nums[i] & mask:
                    count_array += 1
                
                # Count bits in the range [1, n]
                if i > 0 and (i & mask):
                    count_range += 1
                    
            # If count in array is greater, this bit belongs to the duplicate
            if count_array > count_range:
                duplicate |= mask
                
        return duplicate


        