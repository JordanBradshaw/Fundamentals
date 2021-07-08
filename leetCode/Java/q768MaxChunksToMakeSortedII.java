package Fundamentals.leetCode.Java;
/*
https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

Runtime: 1 ms, faster than 76.83% of Java online submissions for Max Chunks To Make Sorted II.
Memory Usage: 38.7 MB, less than 48.46% of Java online submissions for Max Chunks To Make Sorted II.

*/
public class q768MaxChunksToMakeSortedII {
    public static int maxChunksToSorted(int[] arr) {
        int[] arrMin = new int[arr.length + 1];
        arrMin[arr.length] = Integer.MAX_VALUE;
        for (int i = arr.length - 1; i >= 0; i--) {
            arrMin[i] = Math.min(arr[i], arrMin[i + 1]);
            //arrMin[i] = val;
        }
        int count = 0, currMax = arr[0];
        for (int i = 0; i < arr.length; i++) {
            currMax = Math.max(currMax, arr[i]);
            if (currMax <= arrMin[i + 1])
                count++;
        }

        return count;
    }

    public static void main(String[] args) {
        maxChunksToSorted(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, });
    }
}
