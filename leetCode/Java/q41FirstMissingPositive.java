import java.util.Arrays;
/*
https://leetcode.com/problems/first-missing-positive/

Runtime: 4 ms, faster than 42.25% of Java online submissions for First Missing Positive.
Memory Usage: 96.8 MB, less than 26.40% of Java online submissions for First Missing Positive.
*/
public class q41FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int value = 0;
        for (int val : nums) {
            if (val <= value)
                continue;
            if ((val - 1) == value)
                value = val;
            else
                break;
        }
        return value + 1;
    }
}
