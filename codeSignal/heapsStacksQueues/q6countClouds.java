package Fundamentals.codeSignal.heapsStacksQueues;

/*
Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), count the number of clouds. A cloud is surrounded by clear sky, and is formed by connecting adjacent clouds horizontally or vertically. You can assume that all four edges of the skyMap are surrounded by clear sky.

*/
public class q6countClouds {
    void neighborOnes(char[][] skyMap, int row, int col) {
        if (skyMap[row][col] != '1')
            return;
        skyMap[row][col] = '2';
        if (row > 0)
            neighborOnes(skyMap, row - 1, col);
        if (row < skyMap.length - 1)
            neighborOnes(skyMap, row + 1, col);
        if (col > 0)
            neighborOnes(skyMap, row, col - 1);
        if (col < skyMap[row].length - 1)
            neighborOnes(skyMap, row, col + 1);
    }

    int countClouds(char[][] skyMap) {
        int count = 0;
        for (int row = 0; row < skyMap.length; row++) {
            for (int col = 0; col < skyMap[row].length; col++) {
                if (skyMap[row][col] == '1') {
                    neighborOnes(skyMap, row, col);
                    count++;
                }
            }
        }
        return count;
    }

    public void main(String[] args) {

    }
}
