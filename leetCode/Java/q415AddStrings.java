package Fundamentals.leetCode.Java;
/*
https://leetcode.com/problems/add-strings/

Runtime: 3 ms, faster than 43.56% of Java online submissions for Add Strings.
Memory Usage: 38.8 MB, less than 87.35% of Java online submissions for Add Strings.
*/

public class q415AddStrings {
    public static String addStrings(String num1, String num2) {
        String rev1 = new StringBuilder(num1).reverse().toString(), rev2 = new StringBuilder(num2).reverse().toString();
        StringBuilder sbRet = new StringBuilder();
        int i1 = 0 , i2 = 0;
        int carryOver = 0;
        while (i1 < num1.length() && i2 < num2.length()) {
            int val = (rev1.charAt(i1)- '0') + (rev2.charAt(i2) - '0') + carryOver; //+ Integer.valueOf(rev2.charAt(i2));
            int rightSide = val % 10;
            sbRet.append(rightSide);
            carryOver = (val >= 10) ? ((val - rightSide) / 10) : 0;
            i1++;
            i2++;
        }
        
        if (i1 != num1.length() && i2 == num2.length()){
            while (i1 < num1.length()) {
                int val = (rev1.charAt(i1)- '0') + carryOver;
                int rightSide = val % 10;
                sbRet.append(rightSide);
                carryOver = (val >= 10) ? ((val - rightSide) / 10) : 0;
                i1++;
            }
        }
        else if (i1 == num1.length() && i2 != num2.length()){
            while (i2 < num2.length()) {
                int val = (rev2.charAt(i2)- '0') + carryOver;
                int rightSide = val % 10;
                sbRet.append(rightSide);
                carryOver = (val >= 10) ? ((val - rightSide) / 10) : 0;
                i2++;
            }
            
        }
        if((i1 == num1.length()) && (i2 == num2.length()) && carryOver != 0) sbRet.append(carryOver);
        return sbRet.reverse().toString();

    }

    public static void main(String[] args) {
        addStrings("11","123");
        }
}
