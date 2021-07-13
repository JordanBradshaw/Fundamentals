

import java.util.HashMap;
/*
https://leetcode.com/problems/verifying-an-alien-dictionary/

Runtime: 1 ms, faster than 52.39% of Java online submissions for Verifying an Alien Dictionary.
Memory Usage: 39 MB, less than 29.48% of Java online submissions for Verifying an Alien Dictionary.
*/
public class q953VerifyinganAlienDictionary {
    public boolean compareStrings(String a, String b, HashMap<Character, Integer> dict) {
        int lengthToUse = Math.min(a.length(), b.length());
        if (a.equals(b))
            return true;
        for (int i = 0; i < lengthToUse; i++) {
            if (a.charAt(i) != b.charAt(i)) {
                int aInt = dict.get(a.charAt(i)), bInt = dict.get(b.charAt(i));
                if (aInt > bInt)
                    return false;
                else
                    return true;
            }
        }

        if (a.length() < b.length())
            return true;

        return false;
    }

    public boolean isAlienSorted(String[] words, String order) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        //Fill Dictionary
        for (int i = 0; i < order.length(); i++)
            map.put(order.charAt(i), i);
        for (int i = 0; i < words.length - 1; i++) {
            if (compareStrings(words[i], words[i + 1], map) == false)
                return false;
        }
        return true;
    }
}
