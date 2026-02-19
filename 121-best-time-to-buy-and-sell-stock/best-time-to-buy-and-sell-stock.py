class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for new_price in prices[1:]:
            if new_price < buy_price:
                buy_price = new_price
            
            max_profit = max(max_profit, new_price-buy_price)

        return max_profit