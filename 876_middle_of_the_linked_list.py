'''
876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    Complexity: 
    time = O(n)
    space = O(n)
    '''
    def middleNode(self, head: ListNode) -> ListNode:
        curr = head 
        arr = []
        
        while curr: 
            arr.append(curr.val)
            curr = curr.next 
            
        return arr[(len(arr))//2:]
