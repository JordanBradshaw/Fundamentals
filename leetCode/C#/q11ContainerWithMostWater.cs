/*
https://leetcode.com/problems/container-with-most-water/

Runtime: 4 ms, faster than 26.08% of Java online submissions for Container With Most Water.
Memory Usage: 78.6 MB, less than 10.09% of Java online submissions for Container With Most Water.
*/

public class Solution {
    public int MaxArea(int[] height) {
        int l = 0, r = height.Length - 1, max = 0;
        while (l < r){
            int area = Math.Min(height[l], height[r]) * (r-l);
            if (height[l] < height[r]) l++;
            else r--;
            max = Math.Max(max,area);
        }
        return max;
    }
}
