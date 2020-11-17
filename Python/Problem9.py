#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

#Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negatives are only on one side regarding palindrome 
        if not(x >= 0):
            return False
        else:
            tempx = x
            reversex = 0
            ##Calculate the reverse keeping it as an int
            while tempx > 0:
                reversex *= 10
                reversex += tempx % 10
                tempx //= 10
            if (x == reversex):
                return True
            else:
                return False
Sol = Solution()
Sol.isPalindrome(121)

# Regarding the follow up this was keeping it as an int
# Runtime: 72 ms, faster than 29.09% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14 MB, less than 73.05% of Python3 online submissions for Palindrome Number.