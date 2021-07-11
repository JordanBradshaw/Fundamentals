import java.util.Stack;

/*
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Runtime: 54 ms, faster than 12.48% of Java online submissions for Minimum Remove to Make Valid Parentheses.
Memory Usage: 62.2 MB, less than 5.65% of Java online submissions for Minimum Remove to Make Valid Parentheses.
*/

public class q1249MinimumRemovetoMakeValidParentheses {
     public static String minRemoveToMakeValid(String s) {
        Stack<Integer> st = new Stack<Integer>();
        String[] chars = new String[s.length()];
        for (int i = 0; i < s.length(); i++){
            chars[i] = String.valueOf(s.charAt(i));
        }
        for (int i =0; i < chars.length; i++){
            if (chars[i].equals("(")) st.push(Integer.valueOf(i));
            else if (chars[i].equals(")")){
                if (!st.isEmpty()) st.pop();
                else chars[i] = "";     
            }
        }
        while(!st.isEmpty()) chars[st.pop()] = "";
        return String.join("", chars);
    }

    public static void main(String[] args) {
        minRemoveToMakeValid("lee(t(c)o)de)");
    }
}
