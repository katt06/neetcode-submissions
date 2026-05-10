class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit = sell - buy

        minBuy = prices[0]
        maxProfit = 0
       
        for sell in prices:
            # max is for ensuring maxProfit is actually bigger than the newly calculated stuff
            maxProfit = max(maxProfit, sell - minBuy)
            # ensures minBuy is always the min
            minBuy = min(sell, minBuy)

        return maxProfit

    

        