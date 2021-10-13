/*

https://leetcode.com/problems/power-of-two/

*/
public class q231PowerofTwo {
    
    public static boolean isPowerOfTwo(int n) {
        if (n <= 0)
            return false;
        while (n > 1) {
            if (n % 2 == 1) {
                return false;
            }
            n = n >> 1;
            System.out.println(n);
        }
        return true;
    }
}
