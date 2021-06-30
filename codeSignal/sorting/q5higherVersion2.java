package Fundamentals.codeSignal.sorting;

import java.util.Deque;
import java.util.LinkedList;

public class q5higherVersion2 {
    static Deque<StringBuilder> createQue(String ver){
        Deque<StringBuilder> dq = new LinkedList<StringBuilder>();
        StringBuilder sb = new StringBuilder();
        for (char c1: ver.toCharArray()){
            if (c1 != '.'){
                sb.append(c1);
            }
            else{
                dq.add(sb);
                sb = new StringBuilder();
            }
        }
        dq.add(sb);
        return dq;
    }
    static int higherVersion2(String ver1, String ver2) {
        Deque<StringBuilder> q1 = createQue(ver1), q2 = createQue(ver2);
        while (!q1.isEmpty() && !q2.isEmpty()){
            int val1 = Integer.parseInt(q1.pollFirst().toString()), val2 = Integer.parseInt(q2.pollFirst().toString());
            if(val1 > val2) return 1;
            else if (val1 < val2) return -1;
        }
        return 0;
    }

    public static void main(String[] args){
        higherVersion2("11.11.11111.111.1.1.1.1.1","1.1.1.1.1.1.1.1");
    }


}
