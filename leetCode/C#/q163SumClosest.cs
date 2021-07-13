import java.util.Arrays;

/*
https://leetcode.com/problems/3sum-closest/

Runtime: 140 ms, faster than 22.86% of C# online submissions for 3Sum Closest.
Memory Usage: 25.6 MB, less than 52.80% of C# online submissions for 3Sum Closest.
*/

public class q163SumClosest {
    public int ThreeSumClosest(int[] nums, int target) {
        int low = Int32.MinValue / 10, high = Int32.MaxValue / 10;
        Array.Sort(nums);
        for (int i = 0; i < nums.Length; i++) {
            int l = i + 1, r = nums.Length - 1;
            while (l < r) {
                int curr = nums[i] + nums[l] + nums[r];
                if (curr < target) {
                    low = Math.Max(low, curr);
                    l++;
                } else if (curr > target) {
                    high = Math.Min(high, curr);
                    r--;
                } else
                    return target;
            }
        }
        if(Math.Abs(target - low) < high - target) {
            return low;
        }
        else return high;
    }
    public static void main(String[] args){
        threeSumClosest(new int[]{-3,-2,-5,3,-4}, -1);
    }
}
