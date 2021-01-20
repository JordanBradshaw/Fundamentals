# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
import re
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        que = deque()
        if not s:
            return True
        for char in s:
            if re.search("[a-zA-Z0-9]", char):
                que.appendleft(char.lower())
        listQue = list(que)
        for i in range(len(listQue) // 2):
            if que[i] != que[len(listQue) - 1 - i]:
                return False
        return True


# Runtime: 192 ms, faster than 5.00% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 19.8 MB, less than 9.09% of Python3 online submissions for Valid Palindrome.
