'''
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #what is the smallest number of coins to make up 0 cent, make up 1 cent, etc...
        #use these smaller subproblems to build up to larger problems 
        
        #DP[0] = smallest number of coins to make up 0 cent 
        #DP[1] = smallest number of coins to make up 1 cent ... etc...
        
        DP = [amount+1] * (amount + 1) #we need amount + 1 slots because it is 0 based, values of amount+1 because we need 
        print(DP)
        DP[0] = 0 

        
        for i in range(0, amount+1): 
            
            for j in range(0, len(coins)): 
                
                if coins[j] <= i: #if current denomination is less than/equal to current amount
                    DP[i] = min(DP[i], 1+DP[i-coins[j]]) #1 takes into account the current denomiation, DP[i-coins[j]] represents the fewest number of coins required for i - coins[j] amount (when we take into account coins[j])
                    
        if DP[amount] <= amount: 
            return DP[amount] 
        else: 
            return -1
