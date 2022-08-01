# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p = head
        q = head
        while q != None and q.next != None:
            p = p.next
            q = q.next.next
        
        return q