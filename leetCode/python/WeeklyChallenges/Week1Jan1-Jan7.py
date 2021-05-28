# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        concatArray = []
        for index in range(len(arr)):
            print(index)
            for item in pieces:
                if item[0] == arr[index]:
                    concatArray += item
                    if len(item) > 1:
                        index += len(item) - 1
                        if index >= len(arr) - 1:
                            break
        if concatArray == arr:
            return True
        else:
            return False
        print((concatArray))


print(
    Solution().canFormArray(
        [7, 3, 11, 62, 17, 53, 13, 73, 85, 48, 5, 90], [[13, 11, 53, 73, 17, 7], [62, 48], [90, 5], [3], [85]]
    )
)

# Runtime: 76 ms
# Memory Usage: 14.6 MB
