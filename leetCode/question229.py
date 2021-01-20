# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Makes a counter object which how how many time each number appears in a dictionary
        newCounter = Counter(nums)
        returnList = []
        # For each dictionary value {number,amount of appearance}
        for x, y in newCounter.items():
            # if number appearance is greater of total number of objects / 3
            if y > (len(nums) / 3):
                returnList.append(x)
        return returnList


print(Solution().majorityElement([1]))
# Runtime: 108 ms, faster than 94.06% of Python3 online submissions for Majority Element II.
# Memory Usage: 15.4 MB, less than 63.31% of Python3 online submissions for Majority Element II.
