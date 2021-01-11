# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listOfDict = []
        uniqueDict = []
        returnList = []
        for word in strs:
            if uniqueDict.count(Counter(word)) < 1:
                uniqueDict.append(Counter(word))
            listOfDict.append(Counter(word))
        for currentDict in uniqueDict:
            tempList = []
            for i in range(len(strs)):
                if currentDict == listOfDict[i]:
                    tempList.append(strs[i])
            returnList.append(tempList)
        return returnList


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Runtime: 7304 ms, faster than 5.09% of Python3 online submissions for Group Anagrams.
# Memory Usage: 25.5 MB, less than 9.06% of Python3 online submissions for Group Anagrams.
