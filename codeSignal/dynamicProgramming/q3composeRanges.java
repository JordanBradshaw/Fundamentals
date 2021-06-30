package Fundamentals.codeSignal.dynamicProgramming;

import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class q3composeRanges {
    String getString(Deque<Integer> ranges) {
        if (ranges.size() == 1)
            return ranges.poll().toString();
        else {
            String retString = ranges.pollFirst().toString() + "->" + ranges.pollLast().toString();
            ranges.clear();
            return retString;
        }
    }

    String[] composeRanges(int[] nums) {
        if (nums.length == 0)
            return new String[0];
        if (nums.length == 1)
            return new String[] { String.valueOf(nums[0]) };

        List<String> retList = new LinkedList<String>();
        Deque<Integer> q = new LinkedList<Integer>();
        for (int i : nums) {
            if (q.isEmpty()) {
                q.add(i);
                continue;
            } else if (i == q.peekLast() + 1)
                q.add(i);
            else {
                retList.add(getString(q));
                q.add(i);
            }
        }
        retList.add(getString(q));
        return retList.toArray(new String[retList.size()]);
    }

}
