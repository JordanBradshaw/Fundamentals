# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tempSet = set(nums)
        if len(tempSet) != len(nums):
            return True
        else:
            return False


sol = Solution()
sol.containsDuplicate([1, 2, 3, 4, 5, 6])

# Runtime: 116 ms, faster than 73.74% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20.4 MB, less than 31.77% of Python3 online submissions for Contains Duplicate.
