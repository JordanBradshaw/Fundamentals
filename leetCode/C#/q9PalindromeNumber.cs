/*
https://leetcode.com/problems/palindrome-number/

Runtime: 60 ms, faster than 84.75% of C# online submissions for Palindrome Number.
Memory Usage: 17.5 MB, less than 30.73% of C# online submissions for Palindrome Number.
*/

public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0) return false;
        char[] nums = x.ToString().ToCharArray();
        int j = nums.Length -1;
        for(int i = 0; i< nums.Length; i++){
            if (nums[i] == nums[j]){
                if(i==j || i== j-1) return true;
                else j--;
            }
            else return false;
        }
        return false;
    }
}
