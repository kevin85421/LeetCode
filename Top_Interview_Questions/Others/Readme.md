# Others
## Overview
*   **Easy:** Q1 ~ Q6
*   **Medium:** 
*   **Worth it:** Q3, Q5, Q6
## Q1: Numbers of 1 Bits
### My Solution
*   integer --> bin string --> traverse the string
*   Inefficient (Integer --> bin string is not necessary)
### LeetCode Solution: [Link](https://leetcode.com/problems/number-of-1-bits/solution/)
*   **Good technique**: Use bit operation to avoid the process (int --> bin string)
```java
public int hammingWeight(int n) {
    int bits = 0;
    int mask = 1;
    for (int i = 0; i < 32; i++) {
        if ((n & mask) != 0) {
            bits++;
        }
        mask <<= 1;
    }
    return bits;
}
```
## Q2: Hamming Distance
### My Solution
*   Use technique in Q1 (LeetCode solution)
## Q3: Reverse Bits
### My Solution
*   Call Python API
### LeetCode Solution: [Link](https://leetcode.com/problems/reverse-bits/solution/)
*   Approach 1: Bit by Bit
    *   `n&1` --> retrieve the rightmost bit in an integer n
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
```
*   Approach 2: Byte by Byte with Memoization
    *  `reverseByte` --> [ref](http://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv)
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023 
        return cache[byte]
```
* Approach 3: Mask and Shift
    * Without loop (use bit operations only)
    * 32-bit --> 2 * 16 bit (switch) --> 4 * 8 bit (switch) ...
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
```
## Q4: Pascal's Triangle
### My Solution:
*   Time --> beat 93.33%
*   Space --> beat 53.39%
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
## Q6: Missing Number
### My Solution:
*   Gauss' Formula (Same as Approach 4)
*   Time Complexity: `O(n)`
*   Space Complexity: `O(1)`
### LeetCode Solution: [Link](https://leetcode.com/problems/missing-number/solution/)
*   Approach 3: Bit Manipulation
    *  **Good technique:** `XOR`
    *  Time Complexity: `O(n)`
    *  Space Complexity: `O(1)` 
```python
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```
*   Approach 4: Gauss' Formula
    *   **Good technique:** `//` operator
    *   Time Complexity: `O(n)`
    *   Space Complexity: `O(1)`
```python
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
```
