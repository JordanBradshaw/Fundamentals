# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def findIndex(tempList: List[int], target: int):
            for i in range(len(tempList)):
                if tempList[i] > target:
                    return i

        returnVal = 0
        if not heights:
            return 0
        elif len(heights) == 1:
            return heights[0]
        sumList, baseList = [], []
        sumList.append(heights[0])
        baseList.append(heights[0])
        print(f"sumList: {sumList} , baseList {baseList}")
        for i in range(1, len(heights)):
            if baseList and heights[i] > baseList[-1]:
                sumList.append(0)
                baseList.append(heights[i])
            elif baseList and heights[i] < baseList[-1]:
                if baseList.count(heights[i]) == 0:
                    placeHolder = findIndex(baseList, heights[i])
                    baseList.insert(placeHolder, heights[i])
                    sumList.insert(placeHolder, 0)
                    preI = i - 1
                    while heights[preI] >= heights[i] and preI >= 0:
                        print(preI)
                        sumList[placeHolder] += heights[i]
                        preI -= 1
            print(f"before add: sumList: {sumList} , baseList {baseList}")

            while baseList and heights[i] < baseList[-1]:
                topVal = sumList.pop()
                baseList.pop()
                if topVal > returnVal:
                    returnVal = topVal
            for i in range(len(baseList)):
                sumList[i] += baseList[i]
            print(returnVal)
            print(f"after add: sumList: {sumList} , baseList {baseList}")
        while sumList:
            topVal = sumList.pop()
            if topVal > returnVal:
                returnVal = topVal
        return returnVal


print(Solution().largestRectangleArea([1, 1]))

# Runtime: 1364 ms, faster than 5.07% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 27.3 MB, less than 11.27% of Python3 online submissions for Largest Rectangle in Histogram.
