# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        ans_head = ListNode(0)
        ans_cur = ans_head

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                ans_cur.next = ListNode(l1.val, None)
                l1 = l1.next
            else:
                ans_cur.next = ListNode(l2.val, None)
                l2 = l2.next
            ans_cur = ans_cur.next
        
        if not l1: ans_cur.next = l2
        if not l2: ans_cur.next = l1
        return ans_head.next