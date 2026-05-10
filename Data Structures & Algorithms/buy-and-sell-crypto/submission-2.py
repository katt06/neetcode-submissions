class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit = sell - buy
        maxDiff = 0
        maxSell = 0
        minBuy = 0
        curDiff = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                curDiff = prices[j] - prices[i]
                if curDiff > maxDiff:
                    maxDiff = curDiff


        return maxDiff
        




    

        