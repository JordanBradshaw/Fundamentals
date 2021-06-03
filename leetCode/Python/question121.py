# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return 0 if prices empty or one element
        if not prices or len(prices) == 1:
            return 0
        differenceList = [0] * (len(prices) - 1)
        # Get the difference of each element and store
        for i in range(1, len(prices)):
            differenceList[i - 1] = prices[i] - prices[i - 1]
        highestStock = [0] * len(differenceList)
        # Start with 0 value so if negative you can just buy no stocks
        accumulator = 0
        for index in range(0, len(differenceList)):
            # AS LONG AS THERES POSITIVE 1 CHANGE KEEP ADDING AND STORING
            if 1 <= accumulator + differenceList[index]:
                accumulator += differenceList[index]
                highestStock[index] = accumulator
            else:
                highestStock[index] = accumulator
                accumulator = 0
        # RETURN THE MAX OF THAT LIST
        return max(highestStock)


# Runtime: 44 ms, faster than 99.95% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15.4 MB, less than 5.86% of Python3 online submissions for Best Time to Buy and Sell Stock.


print(Solution().maxProfit([1, 2]))
