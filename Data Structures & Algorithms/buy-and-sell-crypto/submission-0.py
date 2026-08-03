class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxProfit=0
        while r<len(prices):
            if prices[r]>prices[l]: 
                # we make a profit if r>l
                # check if profit is greater than max
                maxProfit=max(maxProfit, prices[r]-prices[l])
            else:
                # profit negative, swap l/r (buy/sell) so we can make profit
                l=r
            r+=1
        return maxProfit