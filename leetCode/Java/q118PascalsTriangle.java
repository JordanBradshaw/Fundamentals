import java.util.ArrayList;
import java.util.List;

/*
https://leetcode.com/problems/pascals-triangle/

Runtime: 1 ms, faster than 35.97% of Java online submissions for Pascal's Triangle.
Memory Usage: 38.7 MB, less than 14.13% of Java online submissions for Pascal's Triangle.
*/

public static class q118PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> retTriangle = new ArrayList<>();
        List<Integer> previousRow = null;
        for (int i = 0; i < numRows; i++) {
            List<Integer> currentRow = new ArrayList<Integer>();
            if (i <= 1) {
                for (int j = 0; j <= i; j++) {
                    currentRow.add(1);
                }
                retTriangle.add(currentRow);
                previousRow = currentRow;
                continue;
            }
            currentRow.add(1);
            for(int k = 1; k < previousRow.size(); k++) {
                int pascal = 0;
                pascal = previousRow.get(k-1) + previousRow.get(k);
                currentRow.add(pascal);
            }
            currentRow.add(1);
            previousRow = currentRow;
            retTriangle.add(currentRow);
        }
        return retTriangle;
    }

    public static void main(String[] args) {

    }
}
