#Difficulty: Medium
#Implement atoi which converts a string to an integer.
#The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#If no valid conversion could be performed, a zero value is returned.
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        signFlag = False
        #Remove whitespace
        s = s.lstrip()
        #STRING CANT BE NOT EMPTY
        if (s == ""):
            return 0
        #STRING CONTAINS NO NUMBERS
        elif (re.search("[0-9]",s) == None):
            return 0
        #DOES NOT START WITH + - OR s[0] !=NUMBER
        elif not(s.startswith('-') or s.startswith('+') or s[0].isdigit()):
            return 0
        #STRIP THE FIRST SIGN
        elif (s.startswith('-')):
            signFlag = True
            s = s[1:]
        elif (s.startswith('+')):
            s = s[1:]
            ##REGEX FILTERS
        if (re.search("^[+].",s) or re.search("^[-].",s) or re.search("^[a-zA-Z]",s) or re.search("[0-9] [0-9]",s) or re.search("\+\s",s) or re.search("\-\s",s)or s.startswith(' ')):
            return 0
        splits = re.split("\s|[a-zA-Z]|\-|\+",s,1)
        if (len(splits) > 1):
            s = splits[0]
        if (re.search("\+\s",s) or re.search("\-\s",s)):
            return 0
        if (re.search("\.",str(s)) != None):
            s = round(float(s))
        s = int(s)
        s = {True :(s*-1), False :s} [signFlag]
        if s < -2 ** 31:
            return -2 ** 31
        elif s > (2 ** 31) - 1:
            return (2 ** 31) - 1
        return s
        
#Runtime: 36 ms, faster than 49.05% of Python3 online submissions for String to Integer (atoi).
#Memory Usage: 14.1 MB, less than 35.39% of Python3 online submissions for String to Integer (atoi).