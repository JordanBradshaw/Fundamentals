# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            for i in nums:
                if i > target:
                    return nums.index(i)
            return len(nums)


varSol = Solution()
print(varSol.searchInsert([1, 3, 5, 6], 2))
# Runtime: 40 ms, faster than 97.48% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15.2 MB, less than 15.20% of Python3 online submissions for Search Insert Position.
