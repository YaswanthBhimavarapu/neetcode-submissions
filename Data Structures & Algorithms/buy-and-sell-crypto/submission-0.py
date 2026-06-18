class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxi_pro = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > maxi_pro:
                    maxi_pro = profit

            else:
                buy = sell
            sell += 1
        return maxi_pro

        