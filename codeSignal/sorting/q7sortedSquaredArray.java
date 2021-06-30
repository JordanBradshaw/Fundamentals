package Fundamentals.codeSignal.sorting;

import java.util.Arrays;

public class q7sortedSquaredArray {
    int[] sortedSquaredArray(int[] array) {
        return Arrays.stream(array).map(x -> x* x).sorted().toArray();
    }
}
