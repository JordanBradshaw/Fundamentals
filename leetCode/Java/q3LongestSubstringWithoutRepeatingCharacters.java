package Fundamentals.leetCode.Java;

import java.util.HashSet;
/*
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Runtime: 125 ms, faster than 9.53% of Java online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 39.2 MB, less than 58.95% of Java online submissions for Longest Substring Without Repeating Characters.


*/
public class q3LongestSubstringWithoutRepeatingCharacters {
    public static int lengthOfLongestSubstring(String s) {
        if (s.length() <= 1)
            return s.length();
        int longSubstringLength = 0;
        for (int i = 0; i < s.length(); i++) {
            HashSet<Character> currentSet = new HashSet<Character>();
            for (int j = i; j < s.length(); j++) {
                if (currentSet.contains(s.charAt(j))) {
                    longSubstringLength = Math.max(longSubstringLength, j - i);
                    break;
                } else if (!currentSet.contains(s.charAt(j)) && j == s.length() - 1)
                    longSubstringLength = Math.max(longSubstringLength, j - i + 1);
                else
                    currentSet.add(s.charAt(j));
            }
        }
        return longSubstringLength;
    }

    public static void main(String[] args) {
        lengthOfLongestSubstring("abcabcbb");
    }
}
