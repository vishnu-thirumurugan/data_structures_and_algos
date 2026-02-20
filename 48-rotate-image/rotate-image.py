class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = [list(reversed(list(i))) for i in zip(*matrix)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = res[i][j]

        