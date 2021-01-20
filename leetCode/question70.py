# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import functools as f
import operator
from itertools import combinations, combinations_with_replacement, permutations


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        stairsList = [0] * n
        stairsList[0] = 1
        stairsList[1] = 2
        for i in range(2, n):
            stairsList[i] = stairsList[i - 1] + stairsList[i - 2]

        print(stairsList)
        return stairsList[n - 1]


sol = Solution()
sol.climbStairs(10)
# Runtime: 28 ms, faster than 80.83% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.3 MB, less than 11.19% of Python3 online submissions for Climbing Stairs.
