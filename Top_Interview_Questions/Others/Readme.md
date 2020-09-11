# Others
## Overview
*   **Easy:** Q1 ~ Q6
*   **Medium:**
*   **Worth it:** Q1
## Q5: Valid Parentheses
### My Solution
*   Same as Approach 1
*   Use `Stack` (LifoQueue)
*   **LifoQueue:** https://www.geeksforgeeks.org/stack-in-python/
*   Time Complexity: `O(n)` --> beat 82.8%
*   Space Complexity: `O(n)` --> beat 18.2%
### LeetCode Solution
*   Approach 1: Stack
    * **Good technique:** Use `return not stack` to replace
```python
if stack.qsize() != 0:
    return False
return True
```