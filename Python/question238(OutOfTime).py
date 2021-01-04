# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnList = []
        leftIndex = []
        rightIndex = []
        for i in range(len(nums)):
            leftIndex = nums[:i]
            rightIndex = nums[i + 1 :]
            left = math.prod(leftIndex)
            right = math.prod(rightIndex)
            returnList.append(left * right)
        return returnList

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        returnList = []
        for i in range(0, len(nums)):
            tempValue = 1
            for j in range(0, len(nums)):
                if i != j:
                    tempValue *= nums[j]
            returnList.append(tempValue)
        return returnList


sol = Solution()
sol.productExceptSelf([1, 2, 3, 4])
