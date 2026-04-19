class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1


        while sell < len(prices):
            if prices[sell] > prices[buy]:
                curr_profit = prices[sell] - prices[buy]
                profit += curr_profit
            
            buy = sell
            sell += 1
        
        return profit
        

