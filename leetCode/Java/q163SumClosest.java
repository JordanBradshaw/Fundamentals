import java.util.Arrays;

/*
https://leetcode.com/problems/3sum-closest/

Runtime: 4 ms, faster than 87.07% of Java online submissions for 3Sum Closest.
Memory Usage: 38.6 MB, less than 57.89% of Java online submissions for 3Sum Closest.
*/

public class q163SumClosest {
    public static int threeSumClosest(int[] nums, int target) {
        int low = Integer.MIN_VALUE / 10, high = Integer.MAX_VALUE / 10;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int curr = nums[i] + nums[l] + nums[r];
                if (curr < target) {
                    low = Math.max(low, curr);
                    l++;
                } else if (curr > target) {
                    high = Math.min(high, curr);
                    r--;
                } else
                    return target;
            }
        }
        if(Math.abs(target - low) < high - target) {
            return low;
        }
        else return high;
        //return Math.min(Math.abs(target - low), high - target);
    }
    public static void main(String[] args){
        threeSumClosest(new int[]{-3,-2,-5,3,-4}, -1);
    }
}
