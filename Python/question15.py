# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        returnList = []
        if len(nums) < 3:
            return []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            leftIndex, rightIndex = i + 1, len(nums) - 1
            while leftIndex < rightIndex:
                threeSum = a + nums[leftIndex] + nums[rightIndex]
                if threeSum > 0:
                    rightIndex -= 1
                elif threeSum < 0:
                    leftIndex += 1
                else:
                    returnList.append([a, nums[leftIndex], nums[rightIndex]])
                    leftIndex += 1
                    while nums[leftIndex] == nums[leftIndex - 1] and leftIndex < rightIndex:
                        leftIndex += 1
        print(returnList)
        return returnList


# Originally ran out of time so got help from the internet
# Runtime: 788 ms, faster than 77.37% of Python3 online submissions for 3Sum.
# Memory Usage: 17.6 MB, less than 35.67% of Python3 online submissions for 3Sum.
