package Fundamentals.leetCode.Java;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
/*
https://leetcode.com/problems/task-scheduler/

Runtime: 32 ms, faster than 19.42% of Java online submissions for Task Scheduler.
Memory Usage: 40.1 MB, less than 73.69% of Java online submissions for Task Scheduler.
*/

public class q621TaskScheduler {
    public static int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : tasks) {
            int count = map.getOrDefault(c, 0) + 1;
            map.put(c, count);
        }
        PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(
                (o1, o2) -> o2.getValue() - o1.getValue());
        pq.addAll(map.entrySet());
        Queue<Map.Entry<Character, Integer>> q = new LinkedList<>();
        int time = 0;
        while (!q.isEmpty() || !pq.isEmpty()) {
            for (int i = 0; i <= n; i++) {
                if (!pq.isEmpty()) {
                    Map.Entry<Character, Integer> count = pq.poll();
                    count.setValue(count.getValue() - 1);
                    time++;
                    if (count.getValue() > 0)
                        q.offer(count);
                } else if (pq.isEmpty() && !q.isEmpty())
                    time++;
            }
            while (!q.isEmpty())
                pq.offer(q.poll());
        }
        return time;
    }

    public static void main(String[] args) {
        leastInterval(new char[]{'A','A','A','A','A','A','B','C','D','E','F','G'},2);
    }
}
