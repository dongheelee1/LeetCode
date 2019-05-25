'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        two pointers per linked list, curr and next 
        '''

        if l1 is None and l2 is None: #if both list are empty, just return None
            return None 
        if l1 is None: #if l1 is empty, return l2
            return l2 
        if l2 is None: #if l2 is empty, return l1 
            return l1 
        
         
        if l1.val > l2.val: #if l1's value is greater than l2's value 
            curr = ListNode(l2.val) #create new node with l2's value 
            curr.next = self.mergeTwoLists(l1, l2.next)
        elif l1.val <= l2.val: 
            curr = ListNode(l1.val) #if l2's value is greater than or equal to l2's value 
            curr.next = self.mergeTwoLists(l1.next, l2) #create new node with l1's value
        
        return curr #the final linked list will be constructed bottom up 
