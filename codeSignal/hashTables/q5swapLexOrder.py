# Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.


def swapLexOrder(stri, pairs):
    pairDict = {}
    stringDict = {}
    takenDict = {}
    charArray = list(stri)
    # charArray = ["0"] * len(stri)
    print(enumerate(charArray))
    # print(charArray)
    for pair in pairs:
        try:
            pairDict[pair[0]].append(pair[1])
        except KeyError:
            pairDict[pair[0]] = [pair[0]]
            pairDict[pair[0]].append(pair[1])
        try:
            pairDict[pair[1]].append(pair[0])
        except KeyError:
            pairDict[pair[1]] = [pair[1]]
            pairDict[pair[1]].append(pair[0])
        # print(pair)
    # print(pairDict)
    for key, value in pairDict.items():
        for currentValue in value:
            if pairDict[currentValue].count(key) == 0:
                pairDict[currentValue].append(key)
        value.sort()
    print(pairDict)
    for value in pairDict.values():
        for i in value:
            try:
                stringDict[charArray[i - 1]].extend(value)
            except:
                stringDict[charArray[i - 1]] = value
            stringDict[charArray[i - 1]] = sorted(set(stringDict[charArray[i - 1]]))
    stringDict = sorted(stringDict.items(), reverse=True)
    for item in stringDict:
        for currentIndexInList in item[1]:
            # print(currentIndexInList)
            try:
                if takenDict[currentIndexInList] != None:
                    pass
            except KeyError:
                takenDict[currentIndexInList] = [item[0]]
                charArray[currentIndexInList - 1] = item[0]
                print(charArray)
                break
        # print(item)
    print(takenDict)
    # charList.append(charArray[i - 1])
    # print(stringDict)
    print(charArray)

    return "".join(charArray)


string1 = "fixmfbhyutghwbyezkveyameoamqoi"
pairs = [[8, 5], [10, 8], [4, 18], [20, 12], [5, 2], [17, 2], [13, 25], [29, 12], [22, 2], [17, 11]]
swapLexOrder(string1, pairs)
