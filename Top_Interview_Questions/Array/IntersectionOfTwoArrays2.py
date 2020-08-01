from collections import defaultdict
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    hash_table = defaultdict(int)
    for i in nums1:
        hash_table[i] += 1
    for i in nums2:
        if hash_table[i] > 0:
            hash_table[i] = hash_table[i] - 1
            res.append(i)
    return res