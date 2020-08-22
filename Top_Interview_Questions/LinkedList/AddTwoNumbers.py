# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        curr = l1
        while curr != None:
            if l2 != None: curr.val = curr.val + l2.val
            if curr.val >= 10:
                if curr.next == None:
                    curr.next = ListNode(1)
                else:
                    curr.next.val += 1
                curr.val -= 10
            if curr.next == None and l2 != None: 
                curr.next = l2.next
                break
            curr = curr.next
            if l2 != None: l2 = l2.next
        return l1