class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0 # buy
        max_profit = 0

        for s in range(1, len(prices)): # sell
            if prices[s] > prices[b]:
                max_profit = max(max_profit, prices[s] - prices[b])
            else:
                b = s
        
        return max_profit
            
