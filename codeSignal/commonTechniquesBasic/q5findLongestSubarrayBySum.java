package Fundamentals.codeSignal.commonTechniquesBasic;

import java.util.Deque;
import java.util.LinkedList;

public class q5findLongestSubarrayBySum {
    public static int[] findLongestSubarrayBySum(int s, int[] arr) {
    Deque<Integer> q = new LinkedList<Integer>();
    int li = 0, ri = 0;
    int accum = 0 ;
    while (li <= ri && accum != s){
        if (accum < s){
        accum += arr[ri++];
        }
        else if (accum > s){
            accum -= arr[li++];
            while(accum + arr[li-1] > s) accum -= arr[ri--];
        }



    }
    return new int[]{li,ri};
}
    public static void main(String[] args) {
        findLongestSubarrayBySum(12,new int[] {1, 2, 3, 7, 5});
    }
}
