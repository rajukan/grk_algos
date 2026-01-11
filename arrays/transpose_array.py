'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]



'''
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                transposed_matrix[c][r] = matrix[r][c]

        print(f"matrix:    {matrix}")
        print(f"transpose: {transposed_matrix}")
        return transposed_matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().transpose(matrix)