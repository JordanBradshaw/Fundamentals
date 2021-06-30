package Fundamentals.codeSignal.dynamicProgramming;

public class q2houseRobber {
    static int houseRobber(int[] nums) {
    int a = 0, b = 0;
    
    for (int m : nums) {
        b = Math.max(m + a, a = b);
    }
    
    return b;
}


    public static void main(String[] args) {
        int[] val = { 155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239,
                85, 146, 73, 55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203,
                238, 239, 217, 212, 241, 242, 157, 79, 133, 66, 36, 165 };
        houseRobber(val);
        return;
    }

}
