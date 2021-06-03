/*
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Runtime: 232 ms, faster than 85.14% of C# online submissions for Running Sum of 1d Array.
Memory Usage: 31.4 MB, less than 53.18% of C# online submissions for Running Sum of 1d Array.
*/


public class Solution
{
    public int[] RunningSum(int[] nums)
    {
        int[] retArr = new int[nums.Length];
        retArr[0] = nums[0];
        if (nums.Length == 1) return retArr;
        for (int i = 1; i < nums.Length; i++)
        {
            ///DOWN RUNNER
            int sumAccum = 0;
            for (int j = i; j >= 0; j--)
            {
                sumAccum += nums[j];
            }
            retArr[i] = sumAccum;
        }
        return retArr;
    }
}
