class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxi_profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]

                maxi_profit = max(maxi_profit , profit)

            else:
                buy = sell

            sell += 1

        return maxi_profit


        