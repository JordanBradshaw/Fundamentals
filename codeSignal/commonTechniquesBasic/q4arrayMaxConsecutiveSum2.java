package Fundamentals.codeSignal.commonTechniquesBasic;

public class q4arrayMaxConsecutiveSum2 {
    public static int arrayMaxConsecutiveSum2(int[] inputArray) {
        int retMax = inputArray[0];
        int retCurr = retMax;
        for (int i = 1; i < inputArray.length; i++) {
            retCurr = Math.max(inputArray[i], retCurr + inputArray[i]);
            retMax = Math.max(retMax, retCurr);
        }
        return retMax;
}

    public static void main(String[] args) {
        arrayMaxConsecutiveSum2(new int[] {-2, 2, 5, -11, 6});
    }

}
