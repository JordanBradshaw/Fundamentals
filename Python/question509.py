# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        # Iterative Way
        # Make a list of 0's length of n
        fibList = [0] * n
        fibList[1] = 1  # Fill index 1 with value 1
        for i in range(2, n):  # For i starting from the value 2 to the value of n
            # Current index value ='s the previous 2 added
            fibList[i] = fibList[i - 1] + fibList[i - 2]
        return fibList[n - 1] + fibList[n - 2]

        # Runtime: 32 ms, faster than 62.21% of Python3 online submissions for Fibonacci Number.
        # Memory Usage: 14.3 MB, less than 38.91% of Python3 online submissions for Fibonacci Number.

        ##RECURSIVE WAY
        def fibRecursive(passedN):
            if passedN == 1:
                return 1
            elif passedN == 0:
                return 0
            return fibRecursive(passedN - 1) + fibRecursive(passedN - 2)


Solution().fib(10)
