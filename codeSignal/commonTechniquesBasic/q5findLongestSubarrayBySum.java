package Fundamentals.codeSignal.commonTechniquesBasic;

public class q5findLongestSubarrayBySum {
    public static int[] findLongestSubarrayBySum(int s, int[] arr) {
        int li = 0, ri = 0;
        int accum = 0;
        while (li <= ri && accum != s) {
            while (ri < arr.length && accum < s) {
                accum = ((accum + arr[ri]) == s) ? accum + arr[ri] : accum + arr[ri++];
            }

            if (accum > s) {
                if (li == ri) {
                    li++;
                    ri++;
                    if (li == arr.length)
                        return new int[] { -1 };
                    accum = arr[li];
                    continue;
                }
                    accum = ((accum - arr[li]) == s) ? accum - arr[li++] : accum - arr[li++];
                while (accum > s && ri > li)
                    accum = ((accum - arr[ri]) == s) ? accum - arr[ri] : accum - arr[ri--];
            }
            if (accum == s) {
                while (li > 0 && arr[li - 1] == 0) {
                    li--;
                }
                while (ri < arr.length - 1 && arr[ri + 1] == 0) {
                    ri++;
                }
            }

        }
        return new int[] { li + 1, ri + 1 };
    }

    public static void main(String[] args) {
        findLongestSubarrayBySum(12,
                new int[] { 1, 2, 3, 7, 5 });
    }
}
