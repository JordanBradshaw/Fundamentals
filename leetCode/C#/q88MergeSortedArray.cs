/*
https://leetcode.com/problems/merge-sorted-array/

Runtime: 236 ms, faster than 74.42% of C# online submissions for Merge Sorted Array.
Memory Usage: 31.3 MB, less than 21.39% of C# online submissions for Merge Sorted Array.
*/

public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        int[] nums1c = (int[])nums1.Clone();
        int l = 0, r = 0;
        for (int i = 0; i < m + n; i++)
        {
            if (l < m && r < n)
            {
                if (nums1c[l] <= nums2[r]) nums1[i] = nums1c[l++];
                else nums1[i] = nums2[r++];
                continue;
            }
            else if (l < m) nums1[i] = nums1c[l++];
            else if (r < n) nums1[i] = nums2[r++];

        }
    }
}
