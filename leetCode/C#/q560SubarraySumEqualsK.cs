/*
https://leetcode.com/problems/subarray-sum-equals-k/

Runtime: 2140 ms, faster than 14.51% of C# online submissions for Subarray Sum Equals K.
Memory Usage: 33.5 MB, less than 80.26% of C# online submissions for Subarray Sum Equals K.
*/

public class Solution {
    public int SubarraySum(int[] nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.Length; i++) {
            int accum = 0;
            for (int j = i; j < nums.Length; j++) {
                accum += nums[j];
                if (accum == k) {
                    count++;
                }
            }
        }
        return count;
    }
}
