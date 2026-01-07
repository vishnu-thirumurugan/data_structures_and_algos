class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # if there are even number of negatives, you can clash them
        # if there is a zero, you can consider it as black hole and sink all negatives there
        # it is handles implicitly, not explicitly
        rows, cols = len(matrix), len(matrix[0])
        min_abs = float('inf')
        negative = 0
        total_sum = 0

        for r in range(rows):
            for c in range(cols):
                val = matrix[r][c]
                if val < 0:
                    negative += 1
                min_abs = min(min_abs, abs(val))  # this min val will be final negative
                total_sum += abs(val)

        return total_sum - 2*min_abs if negative % 2 == 1 else total_sum





        