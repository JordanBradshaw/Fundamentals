# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        counter = 0
        while counter * counter <= num:
            if num == counter * counter:
                return True
            elif num < counter * counter:
                return False
            else:
                counter += 1


sol = Solution()
sol.isPerfectSquare(4)
# Runtime: 60 ms, faster than 5.66% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 14.3 MB, less than 32.60% of Python3 online submissions for Valid Perfect Square.
