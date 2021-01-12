# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#    Each row must contain the digits 1-9 without repetition.
#    Each column must contain the digits 1-9 without repetition.
#    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
from collections import Counter
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3x3 Scan
        for xaxis in range(3):  # SCALER
            for yaxis in range(3):  # SCALER
                tempDict = {}
                for i in range(3):
                    for j in range(3):
                        currentX = (xaxis * 3) + i
                        currentY = (yaxis * 3) + j
                        currentValue = board[currentX][currentY]
                        if currentValue is not ".":
                            try:
                                tempDict[currentValue] = tempDict[currentValue] + 1
                            except KeyError:
                                tempDict.update({currentValue: 1})
                        # print(currentValue)
                    print(tempDict.values())  #
                    for item in tempDict.values():
                        if item > 1:
                            return False
        ########################################################################
        for row in board:
            tempCounter = Counter(row)
            tempCounter.pop(".")
            for item in tempCounter.values():
                if item > 1:
                    return False
        ########################################################################
        for columnx in range(9):
            tempDict = {}
            for columny in range(9):

                currentValue = board[columny][columnx]
                if currentValue is not ".":
                    try:
                        tempDict[currentValue] = tempDict[currentValue] + 1
                    except KeyError:
                        tempDict.update({currentValue: 1})
                print(tempDict)
            for item in tempDict.values():
                if item > 1:
                    return False

        return True


print(
    Solution().isValidSudoku(
        board=[
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
)


# Runtime: 220 ms, faster than 5.44% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 14.5 MB, less than 14.62% of Python3 online submissions for Valid Sudoku.
