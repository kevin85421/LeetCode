# Sorting and Searching
## Overview
*  **Easy:** Q1~Q2
## Q1: Merge Sorted Array 
### My Solution
*   Use two pointer technique from the end of the lists
```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```
### LeetCode Solution: [Link](https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/discuss/29503/Beautiful-Python-Solution)
*   More concise version:
```python
def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
```