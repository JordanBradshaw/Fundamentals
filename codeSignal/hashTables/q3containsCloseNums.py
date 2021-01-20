# Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.
def containsCloseNums(nums, k):
    valueDict = {}
    for index, key in enumerate(nums):
        try:
            valueDict[key].append(index)
        except KeyError:
            valueDict[key] = [index]
    for key, values in valueDict.items():
        if len(values) > 1:
            possibleCombinations = [(i, j) for i in values for j in values if i != j]
            print(possibleCombinations)
            for i, j in possibleCombinations:
                if abs(i - j) <= k:
                    print(i, j)
                    return True
    return False


nums = [99, 99]
k = 2
containsCloseNums(nums, k)
