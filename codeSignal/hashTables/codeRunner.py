def calculateSum(currentList):
    accumulatorSum = 0
    for i in range(len(currentList)):
        # if i == 2:
        # print(currentList[i] * coins[i])
        accumulatorSum += currentList[i] * coins[i]
    if accumulatorSum > 30000:
        pass
        # print(accumulatorSum)
    return accumulatorSum


coins = [10, 50, 100, 500]
quantity = [4, 4, 4, 4]
coinJar = {}
items = len(quantity)
middleWindowSize = 1
while middleWindowSize < items:
    print(middleWindowSize)
    incArray = [0] * items
    for i in range(items):
        if quantity[i] < 3:
            continue
        for stickIndex in range(quantity[i]):
            if stickIndex < 2:
                continue
            incArray[i] = stickIndex
            for loopNonIndex in range(items - 1):
                print(i, stickIndex, incArray[i], quantity[i])
                for iRunner in range(1, middleWindowSize + 1):
                    upIndex = i + iRunner + loopNonIndex
                    upIndex %= items
                    while incArray[upIndex] < quantity[upIndex]:
                        coinJar[calculateSum(incArray)] = 1
                        # print(calculateSum(incArray))
                        incArray[upIndex] += 1
                        print(incArray)
                    coinJar[calculateSum(incArray)] = 1
                    upIndex += 1
                    if items > 1:
                        upIndex %= items
                for iRunner in range(1, middleWindowSize + 1):
                    downIndex = i + iRunner + loopNonIndex
                    downIndex %= items
                    while incArray[downIndex] > 0:
                        coinJar[calculateSum(incArray)] = 1
                        # print(calculateSum(incArray))
                        incArray[downIndex] -= 1
                        print(incArray)
                    coinJar[calculateSum(incArray)] = 1
                    downIndex += 1
                    if items > 1:
                        downIndex %= items
            incArray[i] += 1
        incArray = [0] * items
    middleWindowSize += 1

    #
