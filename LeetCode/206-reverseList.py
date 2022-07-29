# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #递归
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        newhead = reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre