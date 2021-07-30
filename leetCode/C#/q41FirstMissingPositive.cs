import java.util.Arrays;
/*
https://leetcode.com/problems/first-missing-positive/

Runtime: 312 ms, faster than 26.29% of C# online submissions for First Missing Positive.
Memory Usage: 47.2 MB, less than 42.43% of C# online submissions for First Missing Positive.
*/
public class q41FirstMissingPositive {
    public int FirstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int value = 0;
        foreach (int val in nums) {
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
