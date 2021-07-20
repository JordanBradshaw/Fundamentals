import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

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
    

    return times;
}

}
