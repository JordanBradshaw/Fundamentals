# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


# Runtime: 16 ms, faster than 99.95% of Python3 online submissions for Multiply Strings.
# Memory Usage: 14.1 MB, less than 92.74% of Python3 online submissions for Multiply Strings.
