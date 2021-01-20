# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
from collections import Counter


def firstNotRepeatingCharacter(s):
    if not s:
        return "_"
    sCount = Counter(s)
    for index in range(len(s)):
        if sCount[s[index]] == 1:
            return s[index]
    return "_"


print(firstNotRepeatingCharacter("abacabaabacaba"))
