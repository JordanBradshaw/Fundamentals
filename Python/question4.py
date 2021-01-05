# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalNums = nums1 + nums2
        print(totalNums)
        totalNums.sort()
        if len(totalNums) % 2 == 0:
            index = len(totalNums) // 2 - 1
            value = (totalNums[index] + totalNums[index + 1]) / 2
            return value
        else:
            index = len(totalNums) // 2
            value = totalNums[index]
            return value


sol = Solution()
sol.findMedianSortedArrays([1], [])

# Runtime: 88 ms, faster than 81.95% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.3 MB, less than 91.42% of Python3 online submissions for Median of Two Sorted Arrays.
