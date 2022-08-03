# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        low = head
        fast = head.next
        while fast != low:
            if fast == None or fast.next == None:
                return False
            fast = fast.next.next
            low = low.next
        return True