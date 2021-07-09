/*
https://leetcode.com/problems/longest-common-prefix/

Runtime: 120 ms, faster than 22.03% of C# online submissions for Longest Common Prefix.
Memory Usage: 25.1 MB, less than 82.93% of C# online submissions for Longest Common Prefix.
*/

public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if (strs.Length == 1) return strs[0];
        StringBuilder sb = new StringBuilder();
        int minLength = Int32.MaxValue;
        foreach (string currSt in strs){
            minLength = Math.Min(minLength, currSt.Length);
        }
        for (int i=0; i < minLength; i++){
            char curr = strs[0][i];
            for( int j=1; j< strs.Length; j++){
                if(strs[j][i] == curr) 
                    continue;
                else return sb.ToString();
            }
            sb.Append(curr);
            
        }
        return sb.ToString();
    }
    
}
