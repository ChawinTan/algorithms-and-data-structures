class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices: return 0
        
        max_profit, min_price = 0, prices[0]
        
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
            
        return max_profit

'''
Conditions - U can only sell a stock after you buy a stock.
This means that you can only profit from the subsequent days

we first set the min_price to the initial value and max_profit to 0.
we can then decide if the profit at min price is larger than profit at
current price.

In the same iteration, we can also decide if the min should change or not.

Since we can only sell after we buy, there will definitely by a better profit if
there is a better min_price than current buying price.

We can use max, min(compare, compare) in dynamic programming to memoize
'''
