import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
/*
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Runtime: 3 ms, faster than 45.73% of Java online submissions for Letter Combinations of a Phone Number.
Memory Usage: 39.7 MB, less than 6.43% of Java online submissions for Letter Combinations of a Phone Number.
*/
public class q17LetterCombinationsofaPhoneNumber {
    public static HashMap<Character, List<String>> buildDictionary() {
        HashMap<Character, List<String>> d = new HashMap<>() {
            {
                put('2', Arrays.asList("a", "b", "c"));
                put('3', Arrays.asList("d", "e", "f"));
                put('4', Arrays.asList("g", "h", "i"));
                put('5', Arrays.asList("j", "k", "l"));
                put('6', Arrays.asList("m", "n", "o"));
                put('7', Arrays.asList("p", "q", "r", "s"));
                put('8', Arrays.asList("t", "u", "v"));
                put('9', Arrays.asList("w", "x", "y", "z"));
            }
        };
        return d;

    }

    public static List<String> letterCombinations(String digits) {
        List<String> retL = new ArrayList<>();

        Queue<StringBuilder> q = new LinkedList<>();
        HashMap<Character, List<String>> dict = buildDictionary();
        for (char c : digits.toCharArray()) {
            if (q.isEmpty()) {
                for (String l : dict.get(c)) {
                    StringBuilder sb = new StringBuilder(l);
                    q.add(sb);
                }
            } else {
                Queue<StringBuilder> tempq = new LinkedList<>();
                while (!q.isEmpty()) {
                    StringBuilder prevSB = q.poll();
                    for (String l : dict.get(c)) {
                        StringBuilder currSB = new StringBuilder(prevSB.toString());
                        currSB.append(l);
                        tempq.add(currSB);
                    }
                }
                q = tempq;
            }
        }
        for (StringBuilder sb : q)
            retL.add(sb.toString());

        return retL;
    }

    public static void main(String[] args) {
        letterCombinations("23");
    }
}
