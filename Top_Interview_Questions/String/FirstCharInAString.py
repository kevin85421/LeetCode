from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = defaultdict(int)
        for element in s:
            hash_table[element] += 1
        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
        return -1