# Math
## Overview
*   **Easy:** Q1 ~ Q4
*   **Medium:**
*   **Worth it:** Q3
## Q3: Power of Three
### My Solution
*   Same as Approach 3
*   Correct
```python
(math.log10(n)/math.log10(3)).is_integer()
```
*   Fail
```python
math.log(243,3) # 4.999999
```
*   Time Complexity: log operation is expensive
*   Space Complexity: `O(1)`
### LeetCode Solution: [Link](https://leetcode.com/problems/power-of-three/solution/)
*   Approach 1: Loop Iteration
    *   Time Complexity: `O(log3(n))`
    *   Space Complexity: `O(1)`
*   Approach 2: Base Conversion
    *   Step1: Use trit (base = 3) to represent the number
        *   ex: 5 (decimal) --> 12 (base = 3)
    *   Step2: Representation = 100000.....0000 --> The number is power of three.    
*   Approach 4: Integer Limitations
    *   INT_MAX = 2147483647
    *   The maximum value of ***n*** that is also a power of three is 1162261467.
```java
public class Solution {
    public boolean isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
}
```