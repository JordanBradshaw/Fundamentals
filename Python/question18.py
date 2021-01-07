# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Notice that the solution set must not contain duplicate quadruplets.
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        returnList = []
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if nums[0] + nums[1] + nums[2] + nums[3] == target:
                returnList.append([nums[0], nums[1], nums[2], nums[3]])
            return returnList
        for i, a in enumerate(nums):
            if i > len(nums) - 4:
                continue
            secondIndex, thirdIndex, lastIndex = i + 1, i + 2, len(nums) - 1
            while secondIndex < thirdIndex <= lastIndex:
                if thirdIndex >= lastIndex:
                    secondIndex += 1
                    while nums[secondIndex] == nums[secondIndex - 1] and secondIndex < len(nums) - 2:
                        secondIndex += 1
                    thirdIndex = secondIndex + 1
                    lastIndex = len(nums) - 1
                    continue
                comparedValue = nums[i] + nums[secondIndex] + nums[thirdIndex] + nums[lastIndex]
                print((i, secondIndex, thirdIndex, lastIndex))
                if comparedValue < target:
                    ## IF 3rd Index is right before last index move second index up one
                    if thirdIndex == lastIndex - 1 and secondIndex != lastIndex - 2:
                        secondIndex += 1
                        thirdIndex = secondIndex + 1
                        lastIndex = len(nums) - 1
                    else:
                        thirdIndex += 1
                elif comparedValue > target:
                    if lastIndex - 1 > secondIndex:
                        lastIndex -= 1
                    else:
                        thirdIndex += 1
                        lastIndex = len(nums) - 1
                else:
                    item = [nums[i], nums[secondIndex], nums[thirdIndex], nums[lastIndex]]
                    print(item)
                    if returnList.count(item) == 0:
                        returnList.append([nums[i], nums[secondIndex], nums[thirdIndex], nums[lastIndex]])
                        continue
                    thirdIndex += 1

            print(returnList)
        return returnList


sol = Solution()
sol.fourSum([-3, -2, 0, 7, 6, 4, 0, 4, -10, 7, -3, 4, 3, 10, 1, 8, 2, 7, 3], 6)


# Runtime: 1480 ms, faster than 13.19% of Python3 online submissions for 4Sum.
# Memory Usage: 14.4 MB, less than 52.19% of Python3 online submissions for 4Sum.
