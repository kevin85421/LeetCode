# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        p = head
        cur = head.next
        n = cur.next
        if n == None:
            cur.next = p
            p.next = None
            return cur
        head.next = None
        while n != None:
            cur.next = p
            p = cur
            cur = n
            n = n.next
        cur.next = p
        return cur