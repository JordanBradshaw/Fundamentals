# You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).
#
# Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

from collections import Counter


def groupingDishes(dishes):
    dictionaryOfCounters = {}
    totalCount = {}
    outerObjects = []
    moreThan2 = []
    returnList = []
    for currentList in dishes:
        temp = currentList.pop(0)
        outerObjects.append(temp)
        tempCounter = Counter(currentList)
        dictionaryOfCounters[temp] = tempCounter
        for x, y in tempCounter.items():
            try:
                totalCount[x] += y
                if moreThan2.count(x) == 0:
                    moreThan2.append(x)
            except KeyError:
                totalCount[x] = y
    moreThan2.sort()
    for key in moreThan2:
        returnList.append([key])
    for i, key2 in enumerate(moreThan2):
        tempList = []
        # print(key)
        for key in outerObjects:
            try:
                if dictionaryOfCounters[key][key2] > 0:
                    tempList.append(key)
            except:
                pass
        tempList.sort()
        returnList[i].extend(tempList)
    return returnList


dishes = [
    ["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
    ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
    ["Quesadilla", "Chicken", "Cheese", "Sauce"],
    ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"],
]

groupingDishes(dishes)
