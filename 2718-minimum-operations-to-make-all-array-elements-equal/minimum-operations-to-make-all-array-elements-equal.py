class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix_sum= [0]*(n+1)

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        
        res = []
        for query in queries:
            
            # o(logn) to group smaller and larger numbers
            left, right = 0, n-1 
            while left < right:
                mid = (left + right)//2
                if nums[mid] < query:
                    left = mid + 1
                else:
                    right = mid

            target_idx = left

            # o(1) suing prefix sum to calculate range sum
            sum1 = prefix_sum[target_idx] - prefix_sum[0]
            sum2 = prefix_sum[n] - prefix_sum[target_idx]

            target1 = target_idx * query
            target2 = (n-target_idx)*query
            print(target_idx)
            min_ops = abs(target1-sum1) + abs(sum2-target2)
            res.append(min_ops)

        return res


                

            

            
                    



            
            
        