import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
/*
https://leetcode.com/problems/employee-free-time/
Runtime: 9 ms, faster than 73.55% of Java online submissions for Employee Free Time.
Memory Usage: 41.1 MB, less than 30.48% of Java online submissions for Employee Free Time.
*/
public class q759EmployeeFreeTime {
    class Interval {
        public int start;
        public int end;

        public Interval() {
        }

        public Interval(int _start, int _end) {
            start = _start;
            end = _end;
        }
    }

    public List<Interval> mergeIntervals(List<Interval> list) {
        List<Interval> retL = new ArrayList<Interval>();
        Interval prevInterval = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            Interval currInterval = list.get(i);
            if (currInterval.start > prevInterval.end) {
                retL.add(prevInterval);
                prevInterval = currInterval;
            } else if (prevInterval.start <= currInterval.start && currInterval.start <= prevInterval.end)
                prevInterval.end = Math.max(prevInterval.end, currInterval.end);
            if (i == list.size() - 1)
                retL.add(prevInterval);
        }
        return retL;

    }

    public List<Interval> offsetIntervals(List<Interval> list) {
        List<Interval> retL = new ArrayList<Interval>();
        for (int i = 1; i < list.size(); i++) {
            Interval tempInterval = new Interval(list.get(i - 1).end, list.get(i).start);
            retL.add(tempInterval);
        }
        return retL;

    }

    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> times = new ArrayList<Interval>();
        for (List<Interval> current : schedule) {
            times.addAll(current);
        }
        times.sort(new Comparator<Interval>() {
            @Override
            public int compare(Interval i1, Interval i2) {
                return Integer.compare(i1.start, i2.start);
            }
        });
        List<Interval> mergedIntervals = mergeIntervals(times);

        return offsetIntervals(mergedIntervals);
    }

}
