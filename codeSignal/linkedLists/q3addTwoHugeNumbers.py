# You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.
# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


from itertools import zip_longest


#
def addTwoHugeNumbers(a, b):
    def addTwoArrays(aArray, bArray):
        largestLength = max(len(aArray), len(bArray))
        returnAdditionArray = [0] * largestLength
        carryValue = 0
        for i, x, y in zip_longest(range(largestLength), aArray, bArray, fillvalue=0):
            if x + y + carryValue > 9 and i < largestLength - 1:
                tempValue = x + y + carryValue
                carryValue = 0
                while tempValue > 9:
                    tempValue -= 10
                    carryValue += 1
                returnAdditionArray[i] = tempValue
            else:
                returnAdditionArray[i] = x + y + carryValue
                carryValue = 0
            ########Last line to append if needed
            if returnAdditionArray[largestLength - 1] > 9:
                tempValue = returnAdditionArray[largestLength - 1]
                carryValue = 0
                while tempValue > 9:
                    tempValue -= 10
                    carryValue += 1
                returnAdditionArray[largestLength - 1] = tempValue
                returnAdditionArray.append(carryValue)
        return returnAdditionArray

    def returnIntList(value):
        returnTempList = []
        for char in str(value):
            returnTempList.append(int(char))
        return returnTempList

    def runningMethod(valueRunner):
        tempRunner = valueRunner
        returnCounter = 0
        while tempRunner:
            returnCounter += 1
            tempRunner = tempRunner.next
        return returnCounter

    def fillArray(valueRunner, passedArray):
        topIndex = len(passedArray) - 1
        tempRunner = valueRunner
        #                                             V       V
        # Overall index                 [ 1,2,3,4,5,6,5,4,7,8,9]
        for i in range(topIndex, 0, -4):
            digitsList = returnIntList(tempRunner.value)
            digitsList.reverse()
            for moveFour in range(len(digitsList), 0, -1):
                passedArray[i - 4 + moveFour] = digitsList[moveFour - 1]
            tempRunner = tempRunner.next

    def buildNodesFromArray(passArray):
        nodeVal = 0
        returnNode = None
        for i in range(len(passArray) - 1, -1, -1):

            if (i) % 4 == 0:
                nodeVal += passArray[i]
                if not returnNode:
                    returnNode = runnerNode = ListNode(nodeVal)
                else:
                    runnerNode.next = ListNode(nodeVal)
                    runnerNode = runnerNode.next
                # print(nodeVal)
                nodeVal = 0
            else:
                # print(passArray[i] * (10 ** (i % 4)))
                nodeVal += passArray[i] * (10 ** (i % 4))
        return returnNode

    aCount = runningMethod(a)
    bCount = runningMethod(b)
    aArray = [0] * (aCount * 4)
    bArray = [0] * (bCount * 4)
    fillArray(a, aArray)
    fillArray(b, bArray)
    # print(f"aCount: {aCount} bCount: {bCount}")
    # print(aArray)
    # print(bArray)
    addedArr = addTwoArrays(aArray, bArray)
    return buildNodesFromArray(addedArr)


origA = ListNode(1234)
origA.next = ListNode(4)
origA.next.next = ListNode(5)

origB = ListNode(100)
origB.next = ListNode(100)
origB.next.next = ListNode(100)

addTwoHugeNumbers(origA, origB)
