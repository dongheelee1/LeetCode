'''
19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        '''
        IDEA: 
        
        have two pointers 
        
        place the first pointer at n+1st node 
        
        then, move up first and second pointers until first is pointing to None 
        
        delete the node of interest 
        '''
        #initialize second and first pointers with dummy node ListNode(0)
        second = first = ListNode(0)
        
        #have the next pointers point to head 
        second.next = first.next = head 
        
        #decrease n  
        while n >= 0: 
            first = first.next 
            n -= 1 
        
        #at this point first is pointing to n+1 position 
        #until first is point to None, increment both pointers  
        while first is not None: 
            first = first.next 
            second = second.next 
        
        #delete the node of interest 
        second.next = second.next.next 
        return head
            
