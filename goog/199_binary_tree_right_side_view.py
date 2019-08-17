'''
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        #HINT: The problem says "ordered from top to bottom". This means we have to use a BFS 
        
        visible = []
        
        if root is None: 
            return visible 
        
        #if tree exists, conduct a BFS 
        
        queue = [] #contains the nodes to explore, initially has just the root 
        queue.append(root)
        
        #conudct BFS 
        while len(queue) != 0: #while there are nodes to explore in the queue
            
            size = len(queue)
            
            for i in range(0, size): #go through each node in the current state of the queue 
                
                current = queue.pop(0) #pop off the first node and explore it 
                
                #if we are at the right-most element, add it to the queue 
                if i == size-1: 
                    visible.append(current.val)
                  
                if current.left: #if there is a left node, then it needs to be explored so add to queue 
                    queue.append(current.left)
                     
                if current.right: #if there is a right node, then it needs to be explored so add to queue 
                    queue.append(current.right)
                    
        return visibleValues
