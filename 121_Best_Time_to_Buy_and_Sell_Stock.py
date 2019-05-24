'''
121. Best Time to Buy and Sell Stock
Easy

2556

121

Favorite

Share
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        IDEA: 
            
            Note: You cannot sell a stock before you buy one 
        
            profit = sell price - buy price
        
            have a variable to store the minimum price and a variable to store the maxprofit 
            
            if price is smaller than min price 
            
            else, if minprice is already smaller then check to see if profit current price - minprice is smaller bigger than maxprofit 
            
            if profit is bigger, set max profit 
        '''
        import sys 
        minprice = sys.maxsize
        
        maxprofit = 0 

        
        for i in range(len(prices)): 
            if prices[i] < minprice: 
                
                minprice = prices[i]

            elif prices[i] - minprice > maxprofit: 
                
                maxprofit = prices[i] - minprice 

        return maxprofit
            
