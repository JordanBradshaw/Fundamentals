# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def preciseCalculate(condensedList: List[int]):
            k = 29
            currentIndex = 0
            differenceList = []
            differenceListSorted = []

            def condensedDriver(currentValue: int, modifiedList: List[int], differenceList: List[int]):
                currentIndex = differenceList.index(currentValue)
                differenceList = differenceList[: currentIndex - 1] + differenceList[currentIndex + 1 :]
                print(differenceList)
                valueCombined = (
                    modifiedList[currentIndex - 1] + modifiedList[currentIndex] + modifiedList[currentIndex + 1]
                )
                modifiedList = modifiedList[: currentIndex - 1] + [valueCombined] + modifiedList[currentIndex + 2 :]
                # print(modifiedList)
                # print(valueCombined)
                # print(modifiedList.index(currentValue))
                return modifiedList, differenceList

            if condensedList[0] <= 0:
                condensedList.pop(0)
            differenceList.append(None)
            for i in range(1, len(condensedList) - 1):
                if (condensedList[i]) < 0:
                    value = condensedList[i - 1] + condensedList[i] + condensedList[i + 1]
                    differenceList.append(value)
                    differenceListSorted.append(value)
                else:
                    differenceList.append(None)
            print(f"Difference Unsorted: {differenceList}")
            differenceListSorted.sort(reverse=True)

            poppedValue = differenceListSorted.pop()
            indexVal = differenceList.index(poppedValue)
            indexVal = (indexVal * 2) + 1
            while currentIndex < k:
                condensedList, differenceList = condensedDriver(
                    differenceListSorted[currentIndex], condensedList, differenceList
                )
                currentIndex += 1
            print(f"condensedList: {condensedList}")
            condensedList.sort(reverse=True)
            value = 0
            for i in range(0, k):
                value += condensedList[i]
            print(value)

            print(f"Sorted: {differenceListSorted}")

        def calculateReturn(currentList: List[int]):
            returnVal = 0
            if len(currentList) < k:
                for index in range(0, len(currentList)):
                    returnVal += currentList[index]
            else:
                for index in range(0, k):
                    returnVal += currentList[index]
            return returnVal

        def toleranceCheck(tolerance: int):
            tempList = []
            jumpInt = 0
            for i in range(0, len(jumpList)):
                if jumpList[i] <= tolerance and jumpInt <= 0:
                    jumpInt = 0
                elif jumpList[i] == tolerance and jumpInt + jumpList[i] < 0:
                    tempList.append(jumpInt)
                    jumpInt = 0
                elif jumpList[i] >= tolerance:
                    jumpInt += jumpList[i]
                else:
                    tempList.append(jumpInt)
                    jumpInt = 0
            if jumpInt > 0:
                tempList.append(jumpInt)
            tempList.sort(reverse=True)
            # print(f"Tolerance: {tolerance} The List:{tempList}")
            return calculateReturn(tempList)

        def greedyCondensedList():
            condensedList = []
            positiveBool = True
            jumpInt = 0
            if jumpList[0] < 0:
                positiveBool = False
            for item in jumpList:
                if item > 0 and positiveBool == True:
                    jumpInt += item
                elif item <= 0 and positiveBool == False:
                    jumpInt += item
                else:
                    condensedList.append(jumpInt)
                    jumpInt = item
                    positiveBool = not (positiveBool)
            condensedList.append(jumpInt)
            print(condensedList)
            return condensedList

        def greedyApply(greedyList: List[int]):
            print(f"Greedy: {greedyList}")
            shorterList = []
            returnList = []
            for i in range(1, len(greedyList) - 1):
                if greedyList[i] < 0:
                    # print(f"{abs(greedyList[i]*2)} to {greedyList[i+1]}")
                    if abs(greedyList[i] * 2) < greedyList[i + 1]:
                        previousItem = shorterList.pop()
                        shorterList.append(greedyList[i] + previousItem)
                    else:
                        shorterList.append(greedyList[i])
                else:
                    shorterList.append(greedyList[i])
                if i == len(greedyList) - 2:
                    shorterList.append(greedyList[i + 1])
            jumpInt = 0
            for i in range(0, len(shorterList)):
                if shorterList[i] >= 0:
                    jumpInt += shorterList[i]
                elif shorterList[i] < 0 and jumpInt <= 0:
                    pass
                else:
                    returnList.append(jumpInt)
                    jumpInt = 0
            if jumpInt > 0:
                returnList.append(jumpInt)
            print(f"Shorter: {shorterList}")
            returnList.sort(reverse=True)
            return calculateReturn(returnList)

        def greedyApplyBig(greedyList: List[int]):
            print(f"Greedy: {greedyList}")
            shorterList = []
            returnList = []
            for i in range(1, len(greedyList) - 1):
                if greedyList[i] < 0:
                    if greedyList[i] + greedyList[i + 1] > 7:
                        previousItem = shorterList.pop()
                        shorterList.append(greedyList[i] + previousItem)
                    else:
                        shorterList.append(greedyList[i])
                else:
                    shorterList.append(greedyList[i])
                if i == len(greedyList) - 2:
                    shorterList.append(greedyList[i + 1])
            jumpInt = 0
            for i in range(0, len(shorterList)):
                if shorterList[i] >= 0:
                    jumpInt += shorterList[i]
                elif shorterList[i] < 0 and jumpInt <= 0:
                    pass
                else:
                    returnList.append(jumpInt)
                    jumpInt = 0
            if jumpInt > 0:
                returnList.append(jumpInt)
            print(f"Shorter: {shorterList}")
            returnList.sort(reverse=True)
            return calculateReturn(returnList)

        def singleRunCheck():
            withoutNegative = []
            withNegative = []
            ## Without Negative
            jumpInt = 0
            for i in range(0, len(jumpList)):
                if jumpList[i] >= 0:
                    jumpInt += jumpList[i]
                elif jumpList[i] < 0 and jumpInt <= 0:
                    pass
                else:
                    withoutNegative.append(jumpInt)
                    jumpInt = 0
            if jumpInt > 0:
                withoutNegative.append(jumpInt)
            withoutNegative.sort(reverse=True)
            ##With Negative as long as not under 0
            jumpInt = 0
            for i in range(0, len(jumpList)):
                if jumpList[i] >= 0:
                    jumpInt += jumpList[i]
                elif i == len(jumpList) - 1 and jumpList[i] < 0:
                    withNegative.append(jumpInt)
                    jumpInt = 0
                elif jumpList[i] < 0 and jumpInt + jumpList[i] > 0:
                    jumpInt += jumpList[i]
                else:
                    withNegative.append(jumpInt)
                    jumpInt = 0
            if jumpInt > 0:
                withNegative.append(jumpInt)
            withNegative.sort(reverse=True)
            print(f"The Length of {len(withoutNegative)}")
            print(f"withoutNegative: {withoutNegative}, withNegative: {withNegative}")
            if calculateReturn(withNegative) > calculateReturn(withoutNegative):
                return calculateReturn(withNegative)
            else:
                return calculateReturn(withoutNegative)

        def jumpCalculator(priceList: List[int]):
            tempArray = []
            for i in range(1, len(priceList)):
                tempArray.append(priceList[i] - priceList[i - 1])
            return tempArray

        if k == 0:
            return 0
        elif prices == []:
            return 0
        jumpList = jumpCalculator(prices)
        rangeList = []
        for i in range(-10, 11):
            rangeList.append(toleranceCheck(i))
        rangeList.append(singleRunCheck())
        if k > 5:
            rangeList.append(greedyApply(greedyCondensedList()))
        if k > 25:
            preciseCalculate(greedyCondensedList())

        # print(rangeList)
        #
        # print(max(rangeList))
        ## print(max(rangeList))
        print(f"JumpList: {jumpList}")
        jumpList.sort(reverse=True)
        print(jumpList)
        return max(rangeList)


# 85 + 39 + 76 + 43 + 43 + 3 + 53 + 57 + 83
# 85 + 39 + 76 + 76 + 3 + 53 + 57 + 83
sol = Solution()
sol.maxProfit(
    29,
    [
        70,
        4,
        83,
        56,
        94,
        72,
        78,
        43,
        2,
        86,
        65,
        100,
        94,
        56,
        41,
        66,
        3,
        33,
        10,
        3,
        45,
        94,
        15,
        12,
        78,
        60,
        58,
        0,
        58,
        15,
        21,
        7,
        11,
        41,
        12,
        96,
        83,
        77,
        47,
        62,
        27,
        19,
        40,
        63,
        30,
        4,
        77,
        52,
        17,
        57,
        21,
        66,
        63,
        29,
        51,
        40,
        37,
        6,
        44,
        42,
        92,
        16,
        64,
        33,
        31,
        51,
        36,
        0,
        29,
        95,
        92,
        35,
        66,
        91,
        19,
        21,
        100,
        95,
        40,
        61,
        15,
        83,
        31,
        55,
        59,
        84,
        21,
        99,
        45,
        64,
        90,
        25,
        40,
        6,
        41,
        5,
        25,
        52,
        59,
        61,
        51,
        37,
        92,
        90,
        20,
        20,
        96,
        66,
        79,
        28,
        83,
        60,
        91,
        30,
        52,
        55,
        1,
        99,
        8,
        68,
        14,
        84,
        59,
        5,
        34,
        93,
        25,
        10,
        93,
        21,
        35,
        66,
        88,
        20,
        97,
        25,
        63,
        80,
        20,
        86,
        33,
        53,
        43,
        86,
        53,
        55,
        61,
        77,
        9,
        2,
        56,
        78,
        43,
        19,
        68,
        69,
        49,
        1,
        6,
        5,
        82,
        46,
        24,
        33,
        85,
        24,
        56,
        51,
        45,
        100,
        94,
        26,
        15,
        33,
        35,
        59,
        25,
        65,
        32,
        26,
        93,
        73,
        0,
        40,
        92,
        56,
        76,
        18,
        2,
        45,
        64,
        66,
        64,
        39,
        77,
        1,
        55,
        90,
        10,
        27,
        85,
        40,
        95,
        78,
        39,
        40,
        62,
        30,
        12,
        57,
        84,
        95,
        86,
        57,
        41,
        52,
        77,
        17,
        9,
        15,
        33,
        17,
        68,
        63,
        59,
        40,
        5,
        63,
        30,
        86,
        57,
        5,
        55,
        47,
        0,
        92,
        95,
        100,
        25,
        79,
        84,
        93,
        83,
        93,
        18,
        20,
        32,
        63,
        65,
        56,
        68,
        7,
        31,
        100,
        88,
        93,
        11,
        43,
        20,
        13,
        54,
        34,
        29,
        90,
        50,
        24,
        13,
        44,
        89,
        57,
        65,
        95,
        58,
        32,
        67,
        38,
        2,
        41,
        4,
        63,
        56,
        88,
        39,
        57,
        10,
        1,
        97,
        98,
        25,
        45,
        96,
        35,
        22,
        0,
        37,
        74,
        98,
        14,
        37,
        77,
        54,
        40,
        17,
        9,
        28,
        83,
        13,
        92,
        3,
        8,
        60,
        52,
        64,
        8,
        87,
        77,
        96,
        70,
        61,
        3,
        96,
        83,
        56,
        5,
        99,
        81,
        94,
        3,
        38,
        91,
        55,
        83,
        15,
        30,
        39,
        54,
        79,
        55,
        86,
        85,
        32,
        27,
        20,
        74,
        91,
        99,
        100,
        46,
        69,
        77,
        34,
        97,
        0,
        50,
        51,
        21,
        12,
        3,
        84,
        84,
        48,
        69,
        94,
        28,
        64,
        36,
        70,
        34,
        70,
        11,
        89,
        58,
        6,
        90,
        86,
        4,
        97,
        63,
        10,
        37,
        48,
        68,
        30,
        29,
        53,
        4,
        91,
        7,
        56,
        63,
        22,
        93,
        69,
        93,
        1,
        85,
        11,
        20,
        41,
        36,
        66,
        67,
        57,
        76,
        85,
        37,
        80,
        99,
        63,
        23,
        71,
        11,
        73,
        41,
        48,
        54,
        61,
        49,
        91,
        97,
        60,
        38,
        99,
        8,
        17,
        2,
        5,
        56,
        3,
        69,
        90,
        62,
        75,
        76,
        55,
        71,
        83,
        34,
        2,
        36,
        56,
        40,
        15,
        62,
        39,
        78,
        7,
        37,
        58,
        22,
        64,
        59,
        80,
        16,
        2,
        34,
        83,
        43,
        40,
        39,
        38,
        35,
        89,
        72,
        56,
        77,
        78,
        14,
        45,
        0,
        57,
        32,
        82,
        93,
        96,
        3,
        51,
        27,
        36,
        38,
        1,
        19,
        66,
        98,
        93,
        91,
        18,
        95,
        93,
        39,
        12,
        40,
        73,
        100,
        17,
        72,
        93,
        25,
        35,
        45,
        91,
        78,
        13,
        97,
        56,
        40,
        69,
        86,
        69,
        99,
        4,
        36,
        36,
        82,
        35,
        52,
        12,
        46,
        74,
        57,
        65,
        91,
        51,
        41,
        42,
        17,
        78,
        49,
        75,
        9,
        23,
        65,
        44,
        47,
        93,
        84,
        70,
        19,
        22,
        57,
        27,
        84,
        57,
        85,
        2,
        61,
        17,
        90,
        34,
        49,
        74,
        64,
        46,
        61,
        0,
        28,
        57,
        78,
        75,
        31,
        27,
        24,
        10,
        93,
        34,
        19,
        75,
        53,
        17,
        26,
        2,
        41,
        89,
        79,
        37,
        14,
        93,
        55,
        74,
        11,
        77,
        60,
        61,
        2,
        68,
        0,
        15,
        12,
        47,
        12,
        48,
        57,
        73,
        17,
        18,
        11,
        83,
        38,
        5,
        36,
        53,
        94,
        40,
        48,
        81,
        53,
        32,
        53,
        12,
        21,
        90,
        100,
        32,
        29,
        94,
        92,
        83,
        80,
        36,
        73,
        59,
        61,
        43,
        100,
        36,
        71,
        89,
        9,
        24,
        56,
        7,
        48,
        34,
        58,
        0,
        43,
        34,
        18,
        1,
        29,
        97,
        70,
        92,
        88,
        0,
        48,
        51,
        53,
        0,
        50,
        21,
        91,
        23,
        34,
        49,
        19,
        17,
        9,
        23,
        43,
        87,
        72,
        39,
        17,
        17,
        97,
        14,
        29,
        4,
        10,
        84,
        10,
        33,
        100,
        86,
        43,
        20,
        22,
        58,
        90,
        70,
        48,
        23,
        75,
        4,
        66,
        97,
        95,
        1,
        80,
        24,
        43,
        97,
        15,
        38,
        53,
        55,
        86,
        63,
        40,
        7,
        26,
        60,
        95,
        12,
        98,
        15,
        95,
        71,
        86,
        46,
        33,
        68,
        32,
        86,
        89,
        18,
        88,
        97,
        32,
        42,
        5,
        57,
        13,
        1,
        23,
        34,
        37,
        13,
        65,
        13,
        47,
        55,
        85,
        37,
        57,
        14,
        89,
        94,
        57,
        13,
        6,
        98,
        47,
        52,
        51,
        19,
        99,
        42,
        1,
        19,
        74,
        60,
        8,
        48,
        28,
        65,
        6,
        12,
        57,
        49,
        27,
        95,
        1,
        2,
        10,
        25,
        49,
        68,
        57,
        32,
        99,
        24,
        19,
        25,
        32,
        89,
        88,
        73,
        96,
        57,
        14,
        65,
        34,
        8,
        82,
        9,
        94,
        91,
        19,
        53,
        61,
        70,
        54,
        4,
        66,
        26,
        8,
        63,
        62,
        9,
        20,
        42,
        17,
        52,
        97,
        51,
        53,
        19,
        48,
        76,
        40,
        80,
        6,
        1,
        89,
        52,
        70,
        38,
        95,
        62,
        24,
        88,
        64,
        42,
        61,
        6,
        50,
        91,
        87,
        69,
        13,
        58,
        43,
        98,
        19,
        94,
        65,
        56,
        72,
        20,
        72,
        92,
        85,
        58,
        46,
        67,
        2,
        23,
        88,
        58,
        25,
        88,
        18,
        92,
        46,
        15,
        18,
        37,
        9,
        90,
        2,
        38,
        0,
        16,
        86,
        44,
        69,
        71,
        70,
        30,
        38,
        17,
        69,
        69,
        80,
        73,
        79,
        56,
        17,
        95,
        12,
        37,
        43,
        5,
        5,
        6,
        42,
        16,
        44,
        22,
        62,
        37,
        86,
        8,
        51,
        73,
        46,
        44,
        15,
        98,
        54,
        22,
        47,
        28,
        11,
        75,
        52,
        49,
        38,
        84,
        55,
        3,
        69,
        100,
        54,
        66,
        6,
        23,
        98,
        22,
        99,
        21,
        74,
        75,
        33,
        67,
        8,
        80,
        90,
        23,
        46,
        93,
        69,
        85,
        46,
        87,
        76,
        93,
        38,
        77,
        37,
        72,
        35,
        3,
        82,
        11,
        67,
        46,
        53,
        29,
        60,
        33,
        12,
        62,
        23,
        27,
        72,
        35,
        63,
        68,
        14,
        35,
        27,
        98,
        94,
        65,
        3,
        13,
        48,
        83,
        27,
        84,
        86,
        49,
        31,
        63,
        40,
        12,
        34,
        79,
        61,
        47,
        29,
        33,
        52,
        100,
        85,
        38,
        24,
        1,
        16,
        62,
        89,
        36,
        74,
        9,
        49,
        62,
        89,
    ],
)