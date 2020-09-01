class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cursor1 = m - 1
        cursor2 = n - 1
        pos = len(nums1) - 1
        while cursor1 >= 0 and cursor2 >= 0:
            if nums1[cursor1] >= nums2[cursor2]:
                nums1[pos] = nums1[cursor1]
                cursor1 -= 1
            else:
                nums1[pos] = nums2[cursor2]
                cursor2 -= 1
            pos -= 1
        if cursor1 < 0:
            while pos >= 0:
                nums1[pos] = nums2[cursor2]
                pos -= 1
                cursor2 -= 1