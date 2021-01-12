# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

from collections import deque
from math import prod
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr = [1] * len(nums)
        rightArr = [1] * len(nums)
        returnArr = [0] * len(nums)
        topI = len(nums) - 1
        leftArr[0] = 1
        for bottomI in range(1, len(nums)):
            print(topI - bottomI)
            leftArr[bottomI] = leftArr[bottomI - 1] * nums[bottomI - 1]
            rightArr[topI - bottomI] = rightArr[topI - bottomI + 1] * nums[topI - bottomI + 1]
        for i in range(len(nums)):
            returnArr[i] = leftArr[i] * rightArr[i]
        return returnArr
        print(leftArr)
        print(rightArr)


sol = Solution()
sol.productExceptSelf([1, 2, 3, 4])
# Runtime: 248 ms, faster than 45.20% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.3 MB, less than 31.35% of Python3 online submissions for Product of Array Except Self.
