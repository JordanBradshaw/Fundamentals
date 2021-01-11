from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j].append(matrix[i].pop(0))
        print(matrix)


Solution().rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Runtime: 64 ms, faster than 6.24% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.3 MB, less than 27.56% of Python3 online submissions for Rotate Image.
