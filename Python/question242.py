# Given two strings s and t , write a function to determine if t is an anagram of s.
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Runtime: 28 ms, faster than 99.40% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 45.20% of Python3 online submissions for Valid Anagram.
