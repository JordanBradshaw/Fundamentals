# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
class Solution:
    def tribonacci(self, n: int) -> int:
        # EXIT CONDITIONS IF TOO SMALL TO AVOID INDEX ERROR
        if n < 2:
            return n
        elif n == 2:
            return 1
        # Allocated array with 0's Fill array with given values
        tribArray = [0] * n
        tribArray[0], tribArray[1], tribArray[2] = 0, 1, 1
        # starting from the 3'rd index add the three previous values and set it to that index
        for i in range(3, n):
            tribArray[i] = tribArray[i - 1] + tribArray[i - 2] + tribArray[i - 3]
        print(tribArray)
        # the returned value for n would be the 3 previous values
        return tribArray[n - 1] + tribArray[n - 2] + tribArray[n - 3]


print(Solution().tribonacci(25))

# Runtime: 24 ms, faster than 93.77% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 14.4 MB, less than 10.84% of Python3 online submissions for N-th Tribonacci Number.
