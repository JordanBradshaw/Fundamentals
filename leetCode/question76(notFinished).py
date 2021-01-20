# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
import queue
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterObj = Counter(t)
        # Unique char count
        count = len(t)
        print(counterObj)
        minWindow = float("inf")  # unbounded value
        q = queue.Queue()
        # INDEX t STRING from 1
        i = I = J = 0
        for j, char in enumerate(s, 1):
            if char in counterObj and counterObj[char] > 0:
                count -= 1
            if char in counterObj:
                counterObj[char] -= 1
            print(counterObj)
            print(j, char)


sol = Solution()
sol.minWindow("abcd", "ab")
