# Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
from itertools import cycle


def areFollowingPatterns(strings, patterns):
    stringDict = {}
    patternsDict = {}
    for currPattern, currString in zip(patterns, strings):
        try:
            if stringDict[currPattern] == currString:
                continue
            else:
                stringDict[currPattern] += currString
                return False
        except KeyError:
            stringDict[currPattern] = currString
        try:
            if patternsDict[currString] == currPattern:
                continue
            else:
                patternsDict[currString] += currPattern
                return False
        except KeyError:
            patternsDict[currString] = currPattern
    return True


strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "c"]
print(areFollowingPatterns(strings, patterns))
