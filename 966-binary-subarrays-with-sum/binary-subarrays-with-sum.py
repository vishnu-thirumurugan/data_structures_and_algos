class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        visited = defaultdict(int)
        currSum = 0
        res = 0
        visited[0] = 1 # base case


        for num in nums:
            currSum += num
            print(currSum, currSum - goal, visited[currSum-goal], visited[currSum])
            res += visited[currSum - goal]
            visited[currSum] += 1

        return res

        