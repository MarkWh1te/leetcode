# 714. Best Time to Buy and Sell Stock with Transaction Fee

# Your are given an array of integers prices,
#  for which the i-th element is the price of a given stock on day i;
#  and a non-negative integer fee representing a transaction fee.

# You may complete as many transactions as you like,
#  but you need to pay the transaction fee for each transaction.
#  You may not buy more than 1 share of a stock at a time
#  (ie. you must sell the stock share before you buy again.)

# Return the maximum profit you can make.

# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
from typing import List


class Solution:
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        """
        wait can be convert from wait and sell 
        sell can be convert from hold
        """
        length = len(prices)
        hold = [float("-inf") for _ in range(length + 1)]
        wait = [0 for _ in range(length + 1)]
        for i in range(1, length + 1):
            hold[i] = max(hold[i - 1], wait[i - 1] - prices[i - 1])
            wait[i] = max(hold[i - 1] + prices[i - 1] - fee, wait[i - 1])
        return wait[len(prices)]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        wait can be convert from wait and sell 
        sell can be convert from hold
        """
        hold = float("-inf")
        wait = 0
        for price in prices:
            hold = max(hold, wait - price)
            wait = max(hold + price - fee, wait)
        return wait


if __name__ == "__main__":
    from util import Test

    s = Solution()
    t = Test(s.maxProfit)
    t.equal(8, [1, 3, 2, 8, 4, 9], 2)
