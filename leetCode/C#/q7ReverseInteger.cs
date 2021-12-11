/*
7. 
https://leetcode.com/problems/reverse-integer/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Runtime: 40 ms, faster than 81.62% of C# online submissions for Reverse Integer.
Memory Usage: 15.1 MB, less than 99.37% of C# online submissions for Reverse Integer.
*/

public class Solution
{
    public int Reverse(int x)
    {
        bool isPositive = true;
        if (x < 0)
        {
            isPositive = false;
            x = x * -1;
        }
        int retX = 0;
        while (x > 0)
        {
            int digit = x % 10;
            checked
            {
                try
                {
                    retX = (retX * 10) + digit;
                }
                catch (OverflowException)
                {
                    retX = 0;
                }
            }
            x /= 10;
        }
        if (isPositive == false)
        {
            checked
            {
                try
                {
                    retX = retX * -1;
                }
                catch (OverflowException)
                {
                    retX = 0;
                }
            }
        }
        return retX;
    }
}
