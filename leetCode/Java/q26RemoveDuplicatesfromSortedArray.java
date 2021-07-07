package Fundamentals.leetCode.Java;

import java.util.Deque;
import java.util.LinkedList;

/*
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Runtime: 2 ms, faster than 13.64% of Java online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 40.4 MB, less than 89.91% of Java online submissions for Remove Duplicates from Sorted Array.

*/
public class q26RemoveDuplicatesfromSortedArray {
    public static int removeDuplicates(int[] nums) {
        if (nums.length <= 1) return nums.length;
        Deque<Integer> q = new LinkedList<Integer>();
        q.add(Integer.valueOf(nums[0]));
        for (int val : nums)
            if (val > q.peekLast()) q.addLast(Integer.valueOf(val));
        int count = q.size();
        int i = 0;
        while (!q.isEmpty()){
            nums[i++] = q.pollFirst();
        }
        return count;
    }
    public static void main(String[] args){
        removeDuplicates(new int[]{0,0,1,1,1,2,2,3,3,4});
    }
}
