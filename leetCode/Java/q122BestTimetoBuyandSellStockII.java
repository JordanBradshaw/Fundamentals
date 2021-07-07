package Fundamentals.leetCode.Java;
/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


Runtime: 1 ms, faster than 65.28% of Java online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 38.1 MB, less than 98.12% of Java online submissions for Best Time to Buy and Sell Stock II.
*/
public class q122BestTimetoBuyandSellStockII {
    public static int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int highestProf = 0;
        for (int i = 1; i < prices.length; ++i) {
            int currentDiff = prices[i] - prices[i-1];
            if ( currentDiff >= 0)
                highestProf += currentDiff;
        }
        return highestProf;
    }
    public static void main(String[] args){
        maxProfit(new int[]{7,1,5,3,6,4});
    }
}
