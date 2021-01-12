# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        topIndex = len(s) - 1
        for bottomIndex in range(len(s) // 2):
            temp = s[bottomIndex]
            s[bottomIndex] = s[topIndex - bottomIndex]
            s[topIndex - bottomIndex] = temp
        print(s)


Solution().reverseString(["h", "e", "l", "l", "o"])
# Runtime: 204 ms, faster than 33.50% of Python3 online submissions for Reverse String.
# Memory Usage: 18.7 MB, less than 17.89% of Python3 online submissions for Reverse String.
