package Fundamentals.codeSignal.sorting;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class q6sortByString {
    HashMap<Integer, Character> buildMap(String t){
        HashMap<Integer, Character> m = new HashMap<Integer, Character>();
        int i = 0;
        for (char letter : t.toCharArray()) m.put(i++, letter);
        return m;
    }
    
    String sortByString(String s, String t) {
        HashMap<Integer, Character> m = buildMap(t);
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (char c : s.toCharArray()) list.add(t.indexOf(c));
        Collections.sort(list);
        StringBuilder sb = new StringBuilder();
        for (Integer i : list) sb.append(m.get(i));
        return sb.toString();
    }
}
