/*
https://leetcode.com/problems/container-with-most-water/

Runtime: 400 ms, faster than 9.31% of C# online submissions for Container With Most Water.
Memory Usage: 44.2 MB, less than 82.87% of C# online submissions for Container With Most Water.
*/

public class q11ContainerWithMostWater {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1, max = 0;
        while (l < r){
            int area = Math.min(height[l], height[r]) * (r-l);
            if (height[l] < height[r]) l++;
            else r--;
            max = Math.max(max,area);
        }
        return max;

    }
}
