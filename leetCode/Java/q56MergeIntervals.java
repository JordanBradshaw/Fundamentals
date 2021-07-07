package Fundamentals.leetCode.Java;
/*
https://leetcode.com/problems/merge-intervals/submissions/

Runtime: 8 ms, faster than 25.57% of Java online submissions for Merge Intervals.
Memory Usage: 41.8 MB, less than 47.32% of Java online submissions for Merge Intervals.
*/
import java.util.Collections;
import java.util.Comparator;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class q56MergeIntervals {
    public static int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) return intervals;
        List<int[]> interList = new LinkedList<int[]>();
        for (int[] interval : intervals){
            interList.add(interval);
        }
        Collections.sort(interList, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        Deque<int[]> q = new LinkedList<int[]>();
        for (int[] interval : interList) {
            if(q.isEmpty()) q.addLast(interval);
            else if((q.peekLast()[0] <= interval[0]) && (q.peekLast()[1] >= interval[1])) continue;
            else if((q.peekLast()[1] >= interval[0]) && (q.peekLast()[1] <= interval[1])){
                q.peekLast()[1] = interval[1];
            }
            else q.addLast(interval);
        }
        return q.toArray(new int[q.size()][]);
    }

    public static void main(String[] args){
        merge(new int[][]{{1,4},{2,3}});

    }
}
