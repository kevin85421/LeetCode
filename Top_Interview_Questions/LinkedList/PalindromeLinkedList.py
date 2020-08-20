# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = self.listLength(head)
        if length == 0: return True
        secondHead = head
        for i in range(int((length-length%2)/2) - (length+1)%2):
            secondHead = secondHead.next
        secondHead.next = self.reverseLinkedlist(secondHead.next)
        secondHead = secondHead.next
        firstHead = head
        for i in range(int((length-length%2)/2)):
            if firstHead.val != secondHead.val:
                return False
            firstHead = firstHead.next
            secondHead = secondHead.next
        return True
        
    def listLength(self, head: ListNode):
        length = 0
        first = head
        while first != None:
            length += 1
            first = first.next
        return length
            
    def reverseLinkedlist(self, head: ListNode) -> ListNode:
        prev = None
        curr = head;
        while curr != None:
            nextTemp = curr.next;
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev