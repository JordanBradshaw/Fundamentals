# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # X,Y INDEX
        currentX, currentY = 0, 0
        # If theres a item in the overall matrix and that item has an item
        if matrix and matrix[0]:
            # Assign the length of those to variables
            xBound = len(matrix[0])
            yBound = len(matrix)
        # While the x index is less than the bound
        while currentX < xBound:
            # This checks the next row index[0] if the int is less than the target just move to the next row
            if (
                currentY < yBound - 1 and matrix[currentY + 1][0] <= target
            ):  # The reason for the -1 is if its the last row looking at the next row will cause an error
                currentY += 1
            else:  # If that value == target then its contained
                if matrix[currentY][currentX] == target:
                    return True
                # If its greater than then its not contained
                elif matrix[currentY][currentX] > target:
                    return False
                # If neither then go to next index
                else:
                    currentX += 1
        # If it finished the whole list then its not contained
        return False
        #


print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=61))

# Runtime: 36 ms, faster than 95.52% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.7 MB, less than 61.84% of Python3 online submissions for Search a 2D Matrix.
