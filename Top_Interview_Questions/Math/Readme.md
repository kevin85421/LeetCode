# Math
## Overview
*   **Easy:** Q1 ~ Q4
*   **Medium:**
*   **Worth it:** Q3, Q4
## Q1: Fizz Buzz
### My Solution
*   Same as Approach 2
*   Time Complexity: `O(n)`
*   Space Complexity: `O(1)`
### LeetCode Solution: [Link](https://leetcode.com/problems/fizz-buzz/solution/)
*   Approach 3: Hash it!
    *  Pros: (1) extensible (2) concise
    *  Time Complexity: `O(n)`
    *  Space Complexity: `O(1)`
```python
class Solution:
    def fizzBuzz(self, n):
        ans = []
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        for num in range(1,n+1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]
            if not num_ans_str:
                num_ans_str = str(num)
            ans.append(num_ans_str)  
        return ans
```
*   Approach 4 (in discussion)
    *   **Good technique**: `temp = 'Fizz' * (i%3 < 1) + 'Buzz' * (i%5 < 1)`
```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            temp = 'Fizz' * (i%3 < 1) + 'Buzz' * (i%5 < 1)
            if temp == "":
                ans.append(str(i))
            else:
                ans.append(temp)
        return ans
```
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
## Q4: Roman to Integer
### My Solution
*   Start from the end of the string
    *   Case1: minus
    *   Case2: add
*   Same as Approach 1   
### LeetCode Solution:
*   Approach 1: [Link](https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/discuss/6542/4-lines-in-Python)
    * **Good technique:** traverse the string from end --> `for c in s[::-1]`
    * **Good technique:** `res, p = res - d[c] if d[c] < d[p] else res + d[c], c` 
```python
d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
def romanToInt(self, s):
    res, p = 0, 'I'
    for c in s[::-1]:
        res, p = res - d[c] if d[c] < d[p] else res + d[c], c
    return res
```