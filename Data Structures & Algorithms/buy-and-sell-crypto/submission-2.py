# Track minimum so far → Calculate current profit → Update maximum profit.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        min_price= prices[0]
        profit= 0

        for i in range(n):
            if prices[i]<min_price:
                min_price= prices[i]
            
            else:
                profit= max(profit, (prices[i]-min_price))
        

        return profit