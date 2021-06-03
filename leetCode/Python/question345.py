# Write a function that takes a string as input and reverse only the vowels of a string.

import re
from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        # IF S IS EMPTY OR NULL RETURN ""
        if not s:
            return ""
        # Create double ended queue
        vowelQueue = deque()
        # Make a list of length s and fill with ""
        returnList = [""] * len(s)
        # For every char in string
        for char in s:
            # (Regex) if that char = vowel (ignoring case)
            if re.search(r"a|e|i|o|u", char, re.IGNORECASE):
                # Append to queue
                vowelQueue.append(char)
        # For index in range from 0 to length of s
        for i in range(len(s)):
            # (Regex) if that char = vowel (ignoring case)
            if re.search(r"a|e|i|o|u", s[i], re.IGNORECASE):
                # Place in return List that value from the queue (LIFO)
                returnList[i] = vowelQueue.pop()
            else:
                # Else place nonvowel into return List
                returnList[i] = s[i]
        # Combine list into string to return
        return "".join(returnList)


print(Solution().reverseVowels("hEllo"))
# Runtime: 268 ms, faster than 5.01% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 14.9 MB, less than 93.40% of Python3 online submissions for Reverse Vowels of a String.
