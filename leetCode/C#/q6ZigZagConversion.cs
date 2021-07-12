import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/*
https://leetcode.com/problems/zigzag-conversion/

Runtime: 116 ms, faster than 35.93% of C# online submissions for ZigZag Conversion.
Memory Usage: 26.9 MB, less than 65.58% of C# online submissions for ZigZag Conversion.
*/

public class Solution {
    class Oscillator {
        int current = 0, top = 0;
        bool down = false;

        public Oscillator(int x) {
            top = x;
        }

        public int GetNext() {
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

    public string Convert(string s, int numRows) {
        if (numRows < 2) return s;
        Oscillator osc = new Oscillator(numRows);
        List<Queue<char>> l = new List<Queue<char>>();
        for (int i = 0; i < numRows; i++) {
            Queue<char> temp = new Queue<char>();
            l.Add(temp);
        }
        int index = 0;
        while (index < s.Length) {
            l[osc.GetNext()].Enqueue(s[index++]);
        }
        StringBuilder sb = new StringBuilder();
        while (l.Count > 0) {
            foreach (char c in l[0]){
                sb.Append(c.ToString());
            }
            //l.get(0).forEach(x-> sb.append(x.toString()));
            l.RemoveAt(0);
        }
        return sb.ToString();
    }
}
