# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
#
# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Try to making the string a list by splitting with " "
        try:
            var = s.split()
            # If theres an Index issue return 0
        except IndexError:
            return 0
        if var:  # If the list is not EMPTY
            return len(var[-1])  # Return the length of the -1(LAST ITEM)
        else:  # If the list is EMPTY
            return 0


Solution().lengthOfLastWord(" ")

# Runtime: 28 ms, faster than 79.89% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.3 MB, less than 62.55% of Python3 online submissions for Length of Last Word.
