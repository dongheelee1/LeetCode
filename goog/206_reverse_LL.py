# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

'''
reverseList 

maintain a stack that holds LL nodes 

set up a dummy variable and pop elements from the stack one by one and create a new LL that is reversed.

return dummy.next 
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        stack = []
        
        while head != None: 
            
            stack.append(head)
            head = head.next 
        
        dummy = ListNode(-1)
        curr = dummy
        while len(stack) != 0: 
            a = stack.pop()
            a.next = None 
            curr.next = a 
            curr = curr.next
        return dummy.next
            
