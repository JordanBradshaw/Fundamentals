/*
https://leetcode.com/problems/subarray-sum-equals-k/

Runtime: 1265 ms, faster than 12.20% of Java online submissions for Subarray Sum Equals K.
Memory Usage: 41.3 MB, less than 67.77% of Java online submissions for Subarray Sum Equals K.
*/

public class q560SubarraySumEqualsK {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int accum = 0;
            for (int j = i; j < nums.length; j++) {
                accum += nums[j];
                if (accum == k) {
                    count++;
                }
            }
        }
        return count;
    }
}
