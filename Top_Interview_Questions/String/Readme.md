# String
## Overview
*   **Easy:** Q1
*   **Worth it:** Q2
## Q1: Reverse String
*   This problem is very easy
## Q2: Reverse Integer
### My Solution:
*   Flow:
    *   Step1: Remove rightmost zeroes of ***x***--> `O(log x)` (`log x / log 10 ~= digits`)
    *   Step2: Append each digit of ***x*** to a list ***l*** --> `O(log x)`
    *   Step3: Compute ***ans*** with ***l*** --> `O(log x)`
*   Time Complexity: `O(log x)` --> Complexity is OK, but this problem can be finished in one pass
*   Space Complexity: `O(log x)` --> Too large
### LeetCode Solution: [Link]()
* Approach 1: Pop and Push Digits & Check before Overflow
  * ***pop*** is the rightmost digit of ***x***
    * `pop > 7` --> `2^31 - 1 = 2147483647`
    * `pop < -8` --> `-2^31 = -2147483648`
  * Time Complexity: `O(log x)` --> It is slower than My Solution(?)
  * Space Complexity: `O(1)` 
```c++
int reverse(int x) {
    int rev = 0;
    while (x != 0) {
        int pop = x % 10;
        x /= 10;
        if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
        if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
        rev = rev * 10 + pop;
    }
    return rev;
}
```
* Approach 2: Convert Integer to String and Reverse [Link](https://medium.com/@oange6214/leetcode-%E6%88%91%E5%9C%A8%E5%A4%B1%E6%95%97%E7%9A%84%E8%B7%AF%E4%B8%8A-part-3-7-reverse-integer-982917ced26b)
  * `[1,-1][x<0]` --> `[1,-1]` is a list, and if
    * ***x*** is less than 0 (***x*** < 0 is true) --> `[1,-1][x<0] == x[1]`
    * ***x*** is more than 0 (***x*** < 0 is false) --> `[1,-1][x<0] == x[0]` 
```python
def reverse(self, x: int) -> int:
    sign = [1,-1][x < 0]
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2**31)-1 < rst < 2**31 else 0
```