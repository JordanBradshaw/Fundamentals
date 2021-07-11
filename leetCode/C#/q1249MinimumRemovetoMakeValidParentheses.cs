
/*
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Runtime: 148 ms, faster than 20.07% of C# online submissions for Minimum Remove to Make Valid Parentheses.
Memory Usage: 43.4 MB, less than 5.06% of C# online submissions for Minimum Remove to Make Valid Parentheses.
*/

public class Solution {
    public string MinRemoveToMakeValid(string s) {
        Stack<int> st = new Stack<int>();
        string[] chars = new string[s.Length];
        for (int i = 0; i < s.Length; i++){
            chars[i] = s[i].ToString();
        }
        for (int i =0; i < chars.Length; i++){
            if (chars[i] == "(") st.Push(i);
            else if (chars[i]==")"){
                if (st.Count > 0) st.Pop();
                else chars[i] = "";     
            }
        }
        while(st.Count > 0) chars[st.Pop()] = "";
        return String.Join("", chars);
    }

    public static void main(String[] args) {
        minRemoveToMakeValid("lee(t(c)o)de)");
    }
}
