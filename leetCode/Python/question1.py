# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j and (nums[i] + nums[j]) == target:
                    tempList = []
                    tempList.append(i)
                    tempList.append(j)
                    return tempList


sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)

# Runtime: 48 ms, faster than 67.83% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 57.13% of Python3 online submissions for Two Sum.
