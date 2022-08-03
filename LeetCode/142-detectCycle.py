# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return
        low = head
        fast = head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            low = low.next
            if fast == low:
                fast = head
                low = low.next
                while fast != low:
                    fast = fast.next
                    low = low.next
                return fast
        return 