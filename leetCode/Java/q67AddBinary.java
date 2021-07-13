/*
https://leetcode.com/problems/add-binary/

Runtime: 5 ms, faster than 24.46% of Java online submissions for Add Binary.
Memory Usage: 39.4 MB, less than 20.01% of Java online submissions for Add Binary.
*/

public class q67AddBinary {
    public static String addBinary(String a, String b) {
        StringBuilder sbR = new StringBuilder(), sbA = new StringBuilder(a), sbB = new StringBuilder(b);
        sbA.reverse();
        sbB.reverse();
        int i = 0, j = 0, carry = 0;
        while (i < sbA.length() & j < sbB.length()) {
            int current = carry + Character.getNumericValue(sbA.charAt(i++))
                    + Character.getNumericValue(sbB.charAt(j++));
            if (current <= 1){
                sbR.append(current);
                carry = 0;}
            else {
                carry = 1;
                sbR.append(current - 2);
            }

        }
        while (i < sbA.length()) {
            int current = carry + Character.getNumericValue(sbA.charAt(i++));
            if (current <= 1){
                sbR.append(current);
                carry = 0;
            }
            else {
                carry = 1;
                sbR.append(current - 2);
            }

        }
        while (j < sbB.length()) {
            int current = carry + Character.getNumericValue(sbB.charAt(j++));
            if (current <= 1){
                sbR.append(current);
                carry = 0;
            }
            else {
                carry = 1;
                sbR.append(current - 2);
            }

        }
        if (carry ==1) sbR.append(1);
        return sbR.reverse().toString();

    }

    public static void main(String[] args) {
        addBinary("01111", "10001");
    }
}
