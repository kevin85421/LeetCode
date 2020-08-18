# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head
        cur = head
        listSize = 1
        while cur.next != None:
            listSize += 1
            cur = cur.next
        targetIndex = listSize - n
        cur = head
        
        # Remove 1st element
        if targetIndex == 0:
            return head.next
        for i in range(targetIndex-1):
            cur = cur.next
        if targetIndex == listSize - 1:
            cur.next = None
            return head
        prev = cur
        cur = cur.next
        prev.next = cur.next
        return head