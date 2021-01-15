# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        newCounter = Counter(nums)
        returnTuple = (0, 0)
        for x, y in newCounter.items():
            if y > returnTuple[1]:
                returnTuple = (x, y)
        return returnTuple[0]


print(Solution().majorityElement([6, 5, 5]))
# Runtime: 164 ms, faster than 73.55% of Python3 online submissions for Majority Element.
# Memory Usage: 15.7 MB, less than 9.68% of Python3 online submissions for Majority Element.
