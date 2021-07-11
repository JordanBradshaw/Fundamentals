/*
https://leetcode.com/problems/number-of-islands/

Runtime: 112 ms, faster than 34.79% of C# online submissions for Number of Islands.
Memory Usage: 28.4 MB, less than 60.23% of C# online submissions for Number of Islands.
*/

public class Solution {
    public void visitNode(int x, int y, char[][] grid){
        grid[y][x] = '0';
        if (x > 0 && grid[y][x-1] == '1') visitNode(x-1,y,grid);
        if (x < (grid[0].Length -1) && grid[y][x+1] == '1') visitNode(x+1,y,grid);
        if (y > 0 && grid[y-1][x] == '1') visitNode(x,y-1,grid);
        if (y < (grid.Length - 1) && grid[y+1][x] == '1') visitNode(x,y+1,grid);
    }
    public int NumIslands(char[][] grid) {
        int count = 0;
        int x = grid[0].Length, y = grid.Length;
        for(int i = 0; i< grid[0].Length; i++){
            for(int j=0 ; j< grid.Length; j++){
                if (grid[j][i] == '1'){
                    count++;
                    visitNode(i,j,grid);
                }
            }
            
        }
        return count;
    }
}
