# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.
#
# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.
#
# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.
#
# Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).


def isCryptSolution(crypt, solution):
    cryptDict = {}
    for item in solution:
        cryptDict[item[0]] = item[1]
    totalKeyAccumulator = 0
    for index in range(len(crypt)):
        currentKeyAccumulator = 0
        tenMultiplyer = len(crypt[index]) - 1
        if cryptDict[crypt[index][0]] == "0" and len(crypt[index]) > 1:
            return False
        for char in crypt[index]:
            currentKeyAccumulator += int(cryptDict[char]) * (10 ** tenMultiplyer)
            tenMultiplyer -= 1
        if index != len(crypt) - 1:
            totalKeyAccumulator += currentKeyAccumulator
        else:
            return totalKeyAccumulator == currentKeyAccumulator


crypt = ["TEN", "TWO", "ONE"]
solution = [["O", "1"], ["T", "0"], ["W", "9"], ["E", "5"], ["N", "4"]]
print(isCryptSolution(crypt, solution))
