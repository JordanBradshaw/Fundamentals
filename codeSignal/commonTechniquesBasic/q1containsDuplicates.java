package Fundamentals.codeSignal.commonTechniquesBasic;

import java.util.HashSet;

public class q1containsDuplicates {
    boolean containsDuplicates(int[] a) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i : a){
            if (!set.contains(i)) set.add(i);
            else{
                return true;
            }
        }
            return false;
        }
    }
