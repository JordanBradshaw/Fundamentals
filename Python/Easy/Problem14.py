#Difficulty: Easy
#Write a function to find the longest common prefix string amongst an array of strings.
from typing import List
#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixArray = []
        if not(0 < len(strs) and len(strs) <= 200):
            return ""
        elif(len(strs) == 1):
            return strs[0]
        elif "" in strs: #EXIT IF EMPTY STRING
            return ""
        #USE LOWEST INDEX AS A BASE VALUE
        lowestStringLength = len(strs[0])
        largestStringLength = len(strs[0])
        for words in strs:
            #GO THROUGH ALL WORDS AND CALCULATE SMALLEST WORD LENGTH
            if len(words) > lowestStringLength:
                largestStringLength = len(words)
            if len(words) < lowestStringLength:
                lowestStringLength = len(words)
        for index in range(largestStringLength):
            #RETURN BECAUSE CANT HAVE A PREFIX LARGER THAN THE SMALLEST WORD
            if ((index) == lowestStringLength):
                return ''.join(prefixArray)
            #INDEX CHARACTER THAT EACH WORD WILL COMPARE TO
            compareChar = strs[0][index]
            ##EXIT ON EMPTY STRING
            for items in strs:
                # IF THEY DO NOT MATCH RETURN THE ARRAY BEFORE NEW CHARACTERS GET APPENDED
                if not(items[index] == compareChar):
                    return ''.join(prefixArray)
            prefixArray.append(compareChar)
        return ''.join(prefixArray)
            
# Runtime: 28 ms, faster than 90.88% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.2 MB, less than 35.12% of Python3 online submissions for Longest Common Prefix.