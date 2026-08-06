class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            cost = prices[i] - min_price
            profit = max(profit, cost)
            min_price = min(min_price, prices[i])
        return profit