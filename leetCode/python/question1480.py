'''
1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Runtime: 56 ms, faster than 9.45% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.5 MB, less than 10.38% of Python3 online submissions for Running Sum of 1d Array.
'''



from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        retList = []
        retList.append(nums[0])
        if len(nums) == 1:
            return retList
        
        for i in range(1,len(nums)):
            retList.append(sum(nums[:i+1]))
        return retList
