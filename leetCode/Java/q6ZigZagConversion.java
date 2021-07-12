import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/*
https://leetcode.com/problems/zigzag-conversion/

Runtime: 11 ms, faster than 41.56% of Java online submissions for ZigZag Conversion.
Memory Usage: 40.1 MB, less than 28.76% of Java online submissions for ZigZag Conversion.
*/

public class q6ZigZagConversion {
    static class Oscillator {
        int current = 0, top = 0;
        boolean down = false;

        public Oscillator(int x) {
            top = x;
        }

        public int getNext() {
            if (down == false) {
                if (current == top - 1) {
                    down = true;
                    return current--;
                } else
                    return current++;
            }
            else{
                if (current == 0){
                    down = false;
                    return current++;
                }
                else return current--;
            }
        }
    }

    public static String convert(String s, int numRows) {
        if (numRows < 2) return s;
        Oscillator osc = new Oscillator(numRows);
        List<Queue<Character>> l = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            Queue<Character> temp = new LinkedList<>();
            l.add(temp);
        }
        int index = 0;
        while (index < s.length()) {
            l.get(osc.getNext()).add(s.charAt(index++));
        }
        StringBuilder sb = new StringBuilder();
        while (l.size() > 0) {
            l.get(0).forEach(x-> sb.append(x.toString()));
            l.remove(0);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        convert("PAYPALISHIRING", 3);
    }
}
