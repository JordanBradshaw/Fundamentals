/*
27. Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Runtime: 232 ms, faster than 81.59% of C# online submissions for Remove Element.
Memory Usage: 31 MB, less than 27.52% of C# online submissions for Remove Element.
*/

public class Solution
{
    public int RemoveElement(int[] nums, int val)
    {
        if (nums.Length == 0) return 0;
        if (nums.Length == 1)
        {
            if (nums[0] == val) return 0;
            else return 1;
        }
        int replaceIndex = 0;
        int elementCounter = 0;
        bool replaceReady = false;

        if (nums[0] == val)
        {
            replaceReady = true;
        }
        else
        {
            elementCounter += 1;
        }

        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] != val)
            {
                elementCounter += 1;
            }
            if (nums[i] == val && replaceReady == false)
            {
                replaceReady = true;
                replaceIndex = i;
            }
            if (replaceReady)
            {
                if (nums[i] != val)
                {
                    nums[replaceIndex] = nums[i];
                    replaceIndex += 1;
                }
            }
        }
        return elementCounter;
    }


}
