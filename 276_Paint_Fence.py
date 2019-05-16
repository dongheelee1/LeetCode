'''
276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
'''
class Solution:
    '''
    DP problem 
    If prev state was diff, then current state can end in diff or same.
    diff(i-1) -> diff(i)
    diff(i-1) -> same(i)

    If prev state was same then current state can only end in diff.
    same(i-1) -> diff(i)
    '''
    def numWays(self, n: int, k: int) -> int:
        
        if n == 0 or k == 0:
            return 0
        
        if n == 1:
            return k
        
        same, dif = 0, k
        
        #to paint the same color --> means prev blocks must have been diff color * 1 (the same color)
        #to paint different color --> prev blocks could have been painted the same or different. In either case, to paint different has k-1 options
        for _ in range(1, n): same, dif = dif, (same + dif) * (k - 1)
            
        return same + dif
