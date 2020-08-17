# String
## Overview
*   **Easy:** Q1 ~ Q9
*   **Medium:** Q10
*   **Worth it:** Q2, Q6, Q9, Q11
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
## Q3: First Unique Character in a String
### My Solution (Good enough):
*   Use HashTable
*   Time Complexity: `O(n)`
*   Space Complexity: `O(1)`
*   Trick: Method 1 is faster than Method 2
```python 
# method 1
hash_table = collections.Counter(s)
# method 2
hash_table = defaultdict(int)
for element in s:
    hash_table[element] += 1
```
## Q4: Valid Anagram
### My Solution (Good enough):
*   Use the trick in Q3
*   Time Complexity: `O(n)`
*   Space Complexity: `O(1)`
## Q5: Valid Palindrome
*   This is not a good question
## Q6: String to Integer (atoi)
### My Solution (Good enough)
*   Trick：`range: [-2^31, 2^31 - 1]` --> Do not calculate the boundary values --> `INT_MAX = 2147483647, INT_MIN = -2147483648`
## Q7: Implement strStr()
### My Solution:
*   Call the Python API `string.find($substring)`
*   [TODO]: KMP algorithm --> [link](https://blog.csdn.net/v_july_v/article/details/7041827)
## Q8: Count and Say
### My Solution (Good enough)
*   Runtime: beat 87.5%
*   Memory: beat 91.8%
## Q9: Longest Common Prefix
### My Solution:
*   Compare each character with same index
### Other Solution: [link](https://www.itread01.com/content/1561738803.html)
```python
def longestCommonPrefix(self, strs):
    import os
    return os.path.commonprefix(strs)
```
```python
def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    if not isinstance(m[0], (list, tuple)):
        m = tuple(map(os.fspath, m))
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1
```
*   `()` is a tuple. (Likewise, `[]` is a list.)
*   Comparison between strings is not based on the length of strings.
    *   Ex: A tuple `t = ('flower','flow','flight')` --> `min(t) == flight` & `max(t) == flower`
    *   Because of the feature, we just need to compare `min(t)` and `max(t)` to get longest common prefix
## Q10: Longest Substring Without Repeating Characters
### My Solution
*   Time Complexity: `O(n^3)` --> Bad
*   Space Complexity: `O(nm)` (***m*** is the size of the charset) --> Bad
### LeetCode Solution: [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/)
*   Approach 2: Sliding Window
    *  Time Complexity: `O(2n)`
    *  Space Complexity: `O(min(m,n))` 
       *  We need `O(k)` space for the sliding window, where ***k*** is the size of the Set. The size of the Set is upper bounded by the size of the string nn and the size of the charset/alphabet ***m***.
    *  `j >= i` --> substring: `s[i:j]`
       *  if `s[j]` is not in the substring --> Move sliding window (***j*** ++)
       *  if `s[j]` is in the substring --> Move sliding window (***i*** ++)
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s);
    hash_table = defaultdict(int)
    ans = 0
    i = 0
    j = 0
    while (i < n and j < n):
        if s[j] not in hash_table:
            hash_table[s[j]]
            j += 1
            ans = max(ans, j - i);
        else:
            del hash_table[s[i]]
            i += 1
    return ans;
```
* Approach 3: Sliding Window Optimized
    * ***index*** : (ASCII character set defines 128 characters) Record the last position that the character appears
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s);
    ans = 0
    index = [0] * 128
    i = 0
    j = 0
    while (i < n and j < n):
        i = max(index[ord(s[j])], i)
        ans = max(ans, j - i + 1)
        index[ord(s[j])] = j + 1
        j += 1
    return ans;
```
## Q11: Longest Palindromic Substring
### LeetCode Solution: [Link](https://leetcode.com/problems/longest-palindromic-substring/solution/)
*   Approach 4: Expand Around Center
    *   Time Complexity: `O(n^2)`
    *   Space Complexity: `O(1)`
    *   `2n - 1` centers (***n*** elements + ***(n-1)*** gaps)
*   Approach 5: Manacher's Algorithm (TODO)   