'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock. Return the maximum profit you can achieve from 
this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Sliding Window Dynamic Programming
'''

class SolutionSlidingWindow:
    def maxProfit(self, prices: list[int]) -> int:
        # start left window at 0 and keep increasing right window to find max local profit
        # if right window price is lower than left window price left window index is changed to right window index
        profit = 0
        left = 0
        local_profit = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            if local_profit < prices[right] - prices[left]:
                local_profit = prices[right] - prices[left]
        return max(profit, local_profit)

# Works but inefficent and times out at huge lists
class SolutionBruteForce:
    def maxProfit(self, prices: list[int]) -> int:
        # run two loops, i till Len(prices) - 2, j from i to len(prices) - 1
        # calculate profit (largest difference) between prices(j) - prices(i)
        # if > existing profit, store profit, i, and j
        # return profit
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                if profit < (prices[j] - prices[i]):
                    profit = prices[j] - prices[i]
        return profit
