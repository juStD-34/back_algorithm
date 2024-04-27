class Solution :
    def maxProfit(self, prices):
        min = prices[0]
        max_profit = 0
        for i in range (1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            max_profit = max(max_profit, prices[i] - min)
        return max_profit
            
