# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        returnList = []
        for preLoad in range(k - 1):  #####PRE LOAD FORLOOP 0 - k-1
            while queue and queue[-1] < nums[preLoad]:
                queue.pop()
            queue.append(nums[preLoad])
        for index in range(k - 1, len(nums)):  ######MAIN LOOP
            while queue and queue[-1] < nums[index]:
                queue.pop()
            queue.append(nums[index])
            returnList.append(queue[0])
            if queue[0] == nums[index - k + 1]:
                queue.popleft()
        print(returnList)
        return returnList


sol = Solution()
sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)

# Runtime: 1492 ms, faster than 55.13% of Python3 online submissions for Sliding Window Maximum.
# Memory Usage: 29.7 MB, less than 79.51% of Python3 online submissions for Sliding Window Maximum.
