'''
dynamic programming 
=> there is a top-down or bottom-up approach 
=> think bottom-up (always think about the base cases) 

What are the base cases? 

climbing 0 stairs means there is 1 way to climb it 

climbing 1 stair means there is 1 way to climb it 
DP[0] = 1 
DP[1] = 1 

DP[2] = DP[2-1] + DP[2-0] = 2
DP[3] = DP[3-1] + DP[3-2] = 3 


initialize DP array of size (n+1) 
initialize 
    DP[0] = 1 
    DP[1] = 1 
loop through until i == n, filling in DP array and return DP[n]

complexities: 
time - O(n) single for loop 
space - O(n) size of DP array
'''

'''
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution:
    
    
    def climbStairs(self, n: int) -> int:
        
        
        DP = [0] * (n+1) #n+1 to account for the 0th index
        
        
        DP[0] = 1
        DP[1] = 1
        
        
        for i in range(2, n+1): 
            
            DP[i] = DP[i-1] + DP[i-2]
            
        return DP[n]
