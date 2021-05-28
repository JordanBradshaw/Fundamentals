# Given an m x n matrix, return all elements of the matrix in spiral order.
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y = 0, 0
        returnList = []
        if matrix:
            if matrix[0]:
                x = len(matrix[0])
                y = len(matrix)  #              -                                                                   1
        # The bounds are outside of my indexs hence -1 so ideally a wall on the outside of the index's        -1  [0 -> len(n)-1]  len(n)
        #                                                                                                          v
        #                                                                                                       len(m)-1
        #                                                                                                         len(m)
        topBound, bottomBound = -1, y
        leftBound, rightBound = -1, x
        finishedFlag = False  # Default starting false
        while not (finishedFlag):  # While not true
            xIndex, yIndex = leftBound + 1, topBound + 1
            #### Right -------------------> through the matrix
            while xIndex < rightBound and not (finishedFlag):
                returnList.append(matrix[yIndex][xIndex])
                if xIndex != rightBound - 1:  # IF its not i index before the bound
                    xIndex += 1  # Up the index
                else:  # Now if it is one before the bound
                    if yIndex + 1 != bottomBound:  # if the y index's next index is not the y bound
                        yIndex += 1  # then move it down one y to down doing the down loop
                    else:
                        finishedFlag = True  # if the y index's next index is the boundary after turning then break because its the final item
                    break
            topBound += 1  # Bring the top bound down one and will blockout the top list
            #### Down (Do what right did but in down direction)
            while yIndex < bottomBound and not (finishedFlag):
                returnList.append(matrix[yIndex][xIndex])
                if yIndex != bottomBound - 1:
                    yIndex += 1
                else:
                    if xIndex - 1 != leftBound:
                        xIndex -= 1
                    else:
                        finishedFlag = True
                    break
            rightBound -= 1
            #### Left
            while xIndex > leftBound and not (finishedFlag):
                returnList.append(matrix[yIndex][xIndex])
                if xIndex != leftBound + 1:
                    xIndex -= 1
                else:
                    if yIndex - 1 != topBound:
                        yIndex -= 1
                    else:
                        finishedFlag = True
                    break
            bottomBound -= 1
            #### Up
            while yIndex > topBound and not (finishedFlag):
                returnList.append(matrix[yIndex][xIndex])
                if yIndex != topBound + 1:
                    yIndex -= 1
                else:
                    if xIndex + 1 != rightBound:
                        xIndex += 1
                    else:
                        finishedFlag = True
                    break
            leftBound += 1
        return returnList


Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# Runtime: 24 ms, faster than 95.99% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.3 MB, less than 56.53% of Python3 online submissions for Spiral Matrix.
