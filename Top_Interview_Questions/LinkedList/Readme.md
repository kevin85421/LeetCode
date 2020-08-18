# Linked List
## Overview
*   **Easy:** Q1 ~ Q6
*   **Medium:**
*   **Worth it:** Q2, Q3, Q4
## Q1: Delete Node in a Linked List
*   This is an idiot question.
## Q2: Remove Nth Node From End of List
### My Solution:
*   Two pass algorithm (Similar with Approach1)
*   Cons: The code is not clean (compare to Approach 1)
### LeetCode Solution: [Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/)
*   Approach 1: Two pass algorithm
    *   Add an auxiliary "dummy" node which points to the list head
    *   First pass: Count ***L*** (size of the list)
    *   Second pass: Remove the `(L-n+1) th` node in the list
    *   Time Complexity: `O(L)` (beat 93%)
    *   Space Complexity: `O(1)` (beat 96%)
*   Approach 2: One pass algorithm
    *   ***Good Technique: *** Use two pointers to get the n-th node from end of the list.
    *   Time Complexity: `O(L)`
    *   Space Complexity: `O(1)`
```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    // Advances first pointer so that the gap between first and second is n nodes apart
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    // Move first to the end, maintaining the gap
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}
```
## Q3: Reverse Linked List
### My Solution
* Similar with Approach1, but my code is not as clean as Approach1
* Time Complexity: `O(n)` (beat 78%)
* Space Complexity: `O(1)`
### LeetCode Solution: [Link](https://leetcode.com/problems/reverse-linked-list/solution/)
*   Approach 1: Iterative approach
    *   Time Complexity: `O(n)`
    *   Space Complexity: `O(1)`
```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}
```
*   Approach 2: Recursive approach [Youtube](https://www.youtube.com/watch?v=MRe3UsRadKw#action=share)
    *   Time Complexity: `O(n)`
    *   Space Complexity: `O(n)`
```java
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}
```
## Q4: Merge Two Sorted Lists
### My Solution:
*   Similar with Approach 1
*   Time (beat 94%)
### Solution [Link](https://blog.csdn.net/fuxuemingzhu/article/details/51291406)
*   Approach 1: 
    *   **Trick**: Check whether the list is empty or not `if not l1: print("l1 is empty")` 
```python
def mergeTwoLists(self, l1, l2):
    head = ListNode(0)
    move = head
    if not l1: return l2
    if not l2: return l1
    while l1 and l2:
        if l1.val < l2.val:
            move.next = l1
            l1 = l1.next
        else:
            move.next = l2
            l2 = l2.next
        move = move.next
    move.next = l1 if l1 else l2
    return head.next
```