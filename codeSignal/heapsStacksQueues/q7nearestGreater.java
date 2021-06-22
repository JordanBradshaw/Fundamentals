package Fundamentals.codeSignal.heapsStacksQueues;

import java.util.ArrayList;
/*
Given an array of integers a, return a new array b using the following guidelines:

    For each index i in b, the value of bi is the index of the aj nearest to ai and is also greater than ai.
    If there are two options for bi, put the leftmost one in bi.
    If there are no options for bi, put -1 in bi.

*/
public class q7nearestGreater {
    int nearestDriver(int[] arr, int target, int index) {
        int bottomIndexRunner = index - 1;
        int topIndexRunner = index + 1;
        while (bottomIndexRunner >= 0 || topIndexRunner < arr.length) {
            if (bottomIndexRunner >= 0) {
                if (arr[bottomIndexRunner] > arr[index])
                    return bottomIndexRunner;
                else
                    bottomIndexRunner--;
            }
            if (topIndexRunner < arr.length) {
                if (arr[topIndexRunner] > arr[index])
                    return topIndexRunner;
                else
                    topIndexRunner++;
            }
        }
        return -1;
    }

    int[] nearestGreater(int[] a) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < a.length; i++) {
            list.add(nearestDriver(a, a[i], i));
        }
        return list.stream().mapToInt(x -> x).toArray();
    }
}
