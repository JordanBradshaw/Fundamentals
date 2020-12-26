# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.


class Solution:
    def isValid(self, s: str) -> bool:
        leftChar = ["[", "{", "("]
        bracketStack = []
        if len(s) < 2:
            return False
        for char in s:
            try:
                if leftChar.index(char) >= 0:
                    bracketStack.append(char)
            except ValueError:
                try:
                    if bracketStack[-1] == "[":
                        if char == "]":
                            bracketStack.pop()
                        else:
                            return False
                    elif bracketStack[-1] == "{":
                        if char == "}":
                            bracketStack.pop()
                        else:
                            return False
                    elif bracketStack[-1] == "(":
                        if char == ")":
                            bracketStack.pop()
                        else:
                            return False
                    else:
                        return False
                except IndexError:
                    return False
        if len(bracketStack) == 0:
            return True
        else:
            return False


# Runtime: 36 ms, faster than 15.95% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.4 MB, less than 5.07% of Python3 online submissions for Valid Parentheses.
