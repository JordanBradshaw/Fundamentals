# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        returnArray = [0] * len(nums)
        returnArray[0] = nums[0]
        for index in range(1, len(nums)):
            if returnArray[index - 1] + nums[index] > nums[index]:
                returnArray[index] = returnArray[index - 1] + nums[index]
            else:
                returnArray[index] = nums[index]
        return max(returnArray)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Runtime: 88 ms, faster than 10.53% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 15.1 MB, less than 13.54% of Python3 online submissions for Maximum Subarray.
