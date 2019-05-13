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
'''
Recursive Solution: 

Time Complexity: O(2^n). Size of the recursion tree will be 2^n (there are 2^n nodes)
Space Complexity: O(n). The depth of the recursion tree can go up to n. 

if n == 0 or n == 1: 
    return 1 

return self.climbStairs(n-1) + self.climbStairs(n-2)
'''

'''
DP Solution
Time Complexity: O(n). 1 forloop. 
Space Complexity: O(n). DP array of size n is used. 
    DP = [0 for x in range(0, n+1)]

    DP[0] = 1 
    DP[1] = 1

    for i in range(2, n + 1): 

        DP[i] = DP[i-1] + DP[i-2]

    return DP[n]
'''

'''
Time Complexity: O(n). 1 forloop. 
Space Complexity: O(1). Constant space is used. 
Fibonacci Number: 

        if n == 0 or n == 1: 
            return 1
        a = 1 #(n-1)
        b = 1 #(n-2)
        for i in range(2, n+1): 
            output = a + b
            b = a 
            a = output

        return output
'''


class Solution:

    def climbStairs(self, n: int) -> int:
        DP = [0 for x in range(0, n + 1)]

        DP[0] = 1
        DP[1] = 1

        for i in range(2, n + 1):
            DP[i] = DP[i - 1] + DP[i - 2]

        return DP[n]
