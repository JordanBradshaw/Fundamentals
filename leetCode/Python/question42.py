# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
from collections import Counter
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        def fillArray(array, counter, value, index):
            for i in range(index, len(height)):
                if array[i] < value:
                    array[i] = value
                if height[i] == value:
                    counter -= 1
                if counter == 0:
                    return (index, i)

        def fillArrayRange(array, value, index, index2):
            for i in range(index, index2 + 1):
                if array[i] < value:
                    array[i] = value

        if not height:
            return 0
        elif len(height) == 1:
            return 0
        differenceHeight = [0] * len(height)
        heatMap = Counter(height)
        highestKeys = []
        for item in sorted(heatMap, key=heatMap.get, reverse=True):
            highestKeys.append(item)
        highestKeys.sort(reverse=True)
        for highKeyIndex in range(len(highestKeys) - 1):
            try:  #### SINGLES VERSION
                if heatMap[highestKeys[highKeyIndex]] == 1 and heatMap[highestKeys[highKeyIndex + 1]] == 1:
                    index1 = height.index(highestKeys[highKeyIndex])
                    index2 = height.index(highestKeys[highKeyIndex + 1])
                    for fill in range(min(index1, index2), max(index1, index2) + 1):
                        if differenceHeight[fill] < min(highestKeys[highKeyIndex], highestKeys[highKeyIndex + 1]):
                            differenceHeight[fill] = min(highestKeys[highKeyIndex], highestKeys[highKeyIndex + 1])
                # TOP = 1 and BOTTOM = > 1
                elif heatMap[highestKeys[highKeyIndex]] == 1 and heatMap[highestKeys[highKeyIndex + 1]] > 1:
                    ## Difference array, howMany? , ofValue?, startingAt?
                    botVal = highestKeys[highKeyIndex + 1]
                    twoNumbers = fillArray(differenceHeight, heatMap[botVal], botVal, height.index(botVal))
                    index1 = height.index(highestKeys[highKeyIndex])
                    if index1 < min(twoNumbers):
                        fillArrayRange(differenceHeight, botVal, index1, min(twoNumbers))
                    elif index1 > max(twoNumbers):
                        fillArrayRange(differenceHeight, botVal, max(twoNumbers), index1)
                # TOP = > 1 and BOTTOM = 1
                elif heatMap[highestKeys[highKeyIndex]] > 1 and heatMap[highestKeys[highKeyIndex + 1]] == 1:
                    ## Difference array, howMany? , ofValue?, startingAt?
                    topVal = highestKeys[highKeyIndex]
                    twoNumbers = fillArray(differenceHeight, heatMap[topVal], topVal, height.index(topVal))
                    index2 = height.index(highestKeys[highKeyIndex + 1])
                    botVal = highestKeys[highKeyIndex + 1]
                    if index2 < min(twoNumbers):
                        fillArrayRange(differenceHeight, botVal, index2, min(twoNumbers))
                    elif index2 > max(twoNumbers):
                        fillArrayRange(differenceHeight, botVal, max(twoNumbers), index2)
                # TOP = > 1 and BOTTOM = 1
                elif heatMap[highestKeys[highKeyIndex]] > 1 and heatMap[highestKeys[highKeyIndex + 1]] > 1:
                    ## Difference array, howMany? , ofValue?, startingAt?
                    topVal = highestKeys[highKeyIndex]
                    bottomVal = highestKeys[highKeyIndex + 1]
                    twoNumbersTop = fillArray(differenceHeight, heatMap[topVal], topVal, height.index(topVal))
                    twoNumbersBottom = fillArray(
                        differenceHeight, heatMap[bottomVal], bottomVal, height.index(bottomVal)
                    )
                    if min(twoNumbersTop) > max(twoNumbersBottom):
                        fillArrayRange(differenceHeight, bottomVal, max(twoNumbersBottom), min(twoNumbersTop))
                    elif max(twoNumbersTop) < min(twoNumbersBottom):
                        fillArrayRange(differenceHeight, bottomVal, max(twoNumbersTop), min(twoNumbersBottom))
            except KeyError:
                pass

        ###RETURN RELATED
        returnVal = 0
        for i in range(len(height)):
            if differenceHeight[i] - height[i] > 0:
                returnVal += differenceHeight[i] - height[i]
        return returnVal


Solution().trap([3, 3, 1, 5, 4, 4, 8])


# Runtime: 7176 ms, faster than 5.01% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 16.3 MB, less than 5.12% of Python3 online submissions for Trapping Rain Water.
