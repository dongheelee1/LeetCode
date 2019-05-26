'''
206. Reverse Linked List
Easy

2286

61

Favorite

Share
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #initialize next, curr pointers as head, initialize prev pointer as None 
        prev = None 
        curr = head
        next = head

        
        #when we are at a point of breaking out of this while loop 
        #curr, next are pointing to None 
        #prev is pointing to the very last node 
        while curr != None: 
            next = next.next 
            curr.next = prev
            prev = curr 
            curr = next
        #set the head to be prev 
        head = prev 

        return head
