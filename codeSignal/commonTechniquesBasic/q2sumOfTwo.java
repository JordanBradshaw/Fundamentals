package Fundamentals.codeSignal.commonTechniquesBasic;

import java.util.Arrays;

public class q2sumOfTwo {
    boolean sumOfTwo(int[] a, int[] b, int v) {
    if (a.length == 0 || b.length == 0) return false;
    Arrays.sort(a);
    Arrays.sort(b);
        for (int i : a)
            for (int j : b){
                if (i + j == v)
                    return true;
                else if (i + j > v) 
                    break;
            }

        return false;
    }

}
