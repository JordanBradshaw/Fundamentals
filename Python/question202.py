# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#    Starting with any positive integer, replace the number by the sum of the squares of its digits.
#    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#    Those numbers for which this process ends in 1 are happy.
#
# Return true if n is a happy number, and false if not.


class Solution:
    def isHappy(self, n: int) -> bool:
        def recursiveDriver(passedInt: int) -> int:
            if passedInt == 1:
                return True
            if passedInt >= 2 and passedInt <= 6:
                return False
            accumulator = 0
            convertedString = str(passedInt)
            for char in convertedString:
                accumulator += int(char) * int(char)
            return recursiveDriver(accumulator)

        return recursiveDriver(n)


Solution().isHappy(7)
# Runtime: 32 ms, faster than 83.32% of Python3 online submissions for Happy Number.
# Memory Usage: 14.4 MB, less than 16.63% of Python3 online submissions for Happy Number.
