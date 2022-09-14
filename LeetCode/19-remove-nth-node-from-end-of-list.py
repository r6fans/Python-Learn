# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        p = q = dummy_head

        for item in range(n + 1):
            p = p.next

        
        while p != None:
            p = p.next
            q = q.next
        
        q.next = q.next.next
    

        return dummy_head.next


