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
## Q2: First Bad Version
### My Solution
*   Binary search
*   Time Complexity: `O(log n)`
*   Space Complexity: `O(1)`
### LeetCode Solutio: [Link](https://leetcode.com/problems/first-bad-version/solution/)
*   Approach 1: Binary search (More concise version)
    * ***Important***: the termination condition of binary search
    * ***Important***:
      * `left + (right - left)/2` --> avoid overflow 
      * `(left + right)/2` --> may cause overflow 
```java
public int firstBadVersion(int n) {
    int left = 1;
    int right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (isBadVersion(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```