# Question 7 Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        if ((-2**31 <= x) and (x <= (2**31 - 1))):
            if (x < 0):
                #Because - was getting flipped causing errors
                x *= -1
                flippedx = int(str(x) [::-1])
                flippedx *= -1
            else:
                flippedx = int(str(x) [::-1])
                #This was for if it overflows after reversing
            if ((-2**31 <= flippedx) and (flippedx <= (2**31 - 1))):
                return flippedx
            else:
                return 0
        else:
            return 0
newSol = Solution()
newSol.reverse(-123)

#Runtime: 32 ms, faster than 59.20% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.1 MB, less than 68.69% of Python3 online submissions for Reverse Integer.