class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0

        total = sum(arr[:k])
        average = total/k
        if average >= threshold:
            ans += 1

        n = len(arr)
        left = 0

        for i in range(k,n):
            total += arr[i]
            total -= arr[left]
            left += 1

            average = total/k

            if average >= threshold:
                ans += 1

        return ans

        