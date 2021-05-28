using System;
/* FIRST TIME USING C# 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Runtime: 316 ms, faster than 12.04% of C# online submissions for Two Sum.
Memory Usage: 32.5 MB, less than 17.63% of C# online submissions for Two Sum.
*/

namespace ns1
{
    class solution
    {
        public static int[] TwoSum(int[] nums, int target)
        {
            int[] returnVar = new int[2];
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    Console.WriteLine(i + " " + j);
                    if (nums[i] + nums[j] == target)
                    {
                        returnVar[0] = i;
                        returnVar[1] = j;
                        return (returnVar);
                    }
                }
            }
            return returnVar;
        }
        public static void Main(string[] args)
        {
            int[] nums = { 2, 7, 11, 15 };
            int tar = 9;
            int[] vs = TwoSum(nums, tar);

        }
    }
}
