import java.util.Comparator;
import java.util.PriorityQueue;
/*
https://leetcode.com/problems/k-closest-points-to-origin/

Runtime: 44 ms, faster than 19.54% of Java online submissions for K Closest Points to Origin.
Memory Usage: 46.4 MB, less than 99.20% of Java online submissions for K Closest Points to Origin.
*/
public class q973KClosestPointstoOrigin {

    public static int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> q = new PriorityQueue<int[]>(points.length, new Comparator<int[]>() {
            public int compare(int[] p1, int[] p2) {
                double p1val = Math.pow(Double.valueOf(p1[0]),2) + Math.pow(Double.valueOf(p1[1]),2);
                double p2val = Math.pow(Double.valueOf(p2[0]),2) + Math.pow(Double.valueOf(p2[1]),2);
                return Double.compare(p1val, p2val);
            }
        });
        for (int[] point : points){
            q.add(point);
        }
        int[][] retClosest = new int[k][2];
        for (int i = 0; i < k; i++) {
            int[] temp = q.poll();
            retClosest[i][0] = temp[0];
            retClosest[i][1] = temp[1];
        }
        return retClosest;
    }
}
