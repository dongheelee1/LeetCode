'''
904. Fruit Into Baskets AKA sliding window technique

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
'''


'''
idea: 

establish
1. what i want to return (number of fruits) 
2. pointer i that moves across the tree and restricts the window on the right side 
3. counter 

4. go through the tree 
 a. add the element as key to the counter and increment count 
 b. while the length of counter is greater than or equal to 3 (more than three types of fruits, so we need to limit to 2) 
  i. decrement the count at tree[i] #####we want to get rid of leftmost element of the window 
  ii. if the count is 0, delete the key from counter 
  iii. move pointer i to the right in the tree
 c. recalculate the max number of fruits (that must have 2 types of fruits)


'''
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        num_fruits = 0 
        i = 0 #pointer that moves right everytime we want to exclude left most element of tree 
        
        count = collections.Counter()
        
        for idx, elem in enumerate(tree): 
            
            print(idx, elem) #each elem is the fruit type 
            
            count[elem] += 1
            
            while len(count) >= 3: 
                
                count[tree[i]] -= 1 
                
                if count[tree[i]] == 0: 
                    
                    del count[tree[i]]
                
                i += 1 #exclude left most element the window if we have more than 3 types of fruits
            num_fruits = max(num_fruits, idx-i+1)
        return num_fruits
