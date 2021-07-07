package Fundamentals.codeSignal.commonTechniquesBasic;

import java.util.TreeSet;

public class q7minSubstringWithAllChars {
    static String minSubstringWithAllChars(String s, String t) {
        if (s == "" || s == null || t == null || t == "") return "";
        int[] count = new int[26];
        TreeSet<Character> totalSet = new TreeSet<Character>();
        for (char c : t.toCharArray()){
            count[c - 'a']++;
            totalSet.add(c);
        }
        int lowestIndex = 0, highestIndex = s.length();
        int minLength = s.length()+1;
        for (int i = 0; i < s.length(); i++){
            if(count[s.charAt(i)-'a'] == 0) continue;
            TreeSet<Character> currentSet = new TreeSet<Character>();
            currentSet.add(s.charAt(i));
            if(currentSet.equals(totalSet)) return String.valueOf(s.charAt(i));
            //count[s.charAt(i)-'a'];
            for (int j = i + 1; j < s.length(); j++){
                if(count[s.charAt(j)-'a'] > 0) currentSet.add(s.charAt(j));
                if (currentSet.equals(totalSet)){
                    if (j-i < minLength){
                        minLength = j - i;
                        lowestIndex = i;
                        highestIndex = j;
                    }
                    break;
                }
            }
        }
        return (minLength == (s.length()+1)) ? t : s.substring(lowestIndex, highestIndex+1);
}
    public static void main(String[] args) {
        minSubstringWithAllChars("adobecodebanc","abc");

    }

}
