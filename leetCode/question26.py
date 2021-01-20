# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentIndex = 0
        previousNumber = None
        while currentIndex < len(nums) - 1:
            # print(f"Index: {currentIndex} and Previous: {previousNumber}")
            if nums[currentIndex] == previousNumber:
                nums.pop(currentIndex)
            else:
                previousNumber = nums[currentIndex]
                currentIndex += 1
        return len(set(nums))

# Runtime: 104 ms, faster than 17.27% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 16.3 MB, less than 7.14% of Python3 online submissions for Remove Duplicates from Sorted Array.
