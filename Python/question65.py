# Validate if a given string can be interpreted as a decimal number.

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        if re.search("\-(\+|\-|e)", s) != None:  # - set
            return False
        elif re.search("\+(\+|\-|e)", s) != None:  # + set
            return False
        elif re.search("e[^\-\+\d]|e$|^e", s) != None:  # e set or ends with e or starts with
            return False
        elif re.search("\.(\+|\-|\.)", s) != None:  # . set
            return False
        elif (
            re.search("^\.e\d|\D\.e\d|\s+e\d", s) != None
        ):  # starts with . e digit set  or not digit . e digit set or whitespace e digit
            return False
        elif re.search("(\+|\-)(\D^\.|$)", s) != None:  # + or - with no value after
            return False
        elif re.search("\.\d*\.", s) != None:  # . digit . set
            return False
        elif re.search("(\D^\.)e|\d(\+|\-)", s) != None:  # Not Digit except . e or digit + or -
            return False
        elif re.search("\d[+-]\d", s) != None:  # not digit + or - digit
            return False
        elif re.search("\S\s+\.", s) != None:  # not whitespace 1ormore whitespace then .
            return False
        elif re.search("e\d+\.\d", s) != None:  # e  1ormore digit . digit
            return False
        elif re.search("e(\+|\-)*\d*\.", s) != None:  # e  (+or-) 0ormore digits .
            return False
        elif re.search("[a-df-zA-Z]", s) != None:  # not a-d or f-Z
            return False
        elif (
            re.search("(e|\+|\-|\.|\d)\s(e|\+|\-|\.|\d)", s) != None
        ):  # not acceptable symbols then whitespace then acceptable symbol
            return False
        elif re.search("\d", s) == None:
            return False
        elif s.count("e") > 1:
            return False
        elif len(s) == 1 and s[0] == " ":
            return False
        return True


sol = Solution()
print(sol.isNumber("7.e-."))


# Runtime: 48 ms, faster than 5.32% of Python3 online submissions for Valid Number.
# Memory Usage: 14.4 MB, less than 6.23% of Python3 online submissions for Valid Number.
