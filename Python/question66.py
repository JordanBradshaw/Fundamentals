# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for i, digit in enumerate(digits):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] == 0 and i == len(digits) - 1:
                digits.append(1)
                break
            elif digits[i] != 0:
                break
        digits.reverse()
        print(str(digits))
        return digits


sol = Solution()
sol.plusOne([9])
# Runtime: 32 ms, faster than 64.32% of Python3 online submissions for Plus One.
# Memory Usage: 14.2 MB, less than 67.64% of Python3 online submissions for Plus One.
