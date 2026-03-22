class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # group indices
        hashMap = defaultdict(list)
        for idx, num in enumerate(nums):
            hashMap[num].append(idx)

        res = [0]*len(nums)

        # for each group process and store results
        for indices in hashMap.values():
            prefix = list(accumulate(indices))

            n = len(indices)

            for idx, i in enumerate(indices):
                left = idx*i - (prefix[idx-1] if idx > 0 else 0)
                right = (prefix[-1] - prefix[idx]) - (n-idx-1)*i

                res[i] = left + right

        return res



        