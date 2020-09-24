class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        mask = 1
        for i in range(32):
            if (x & mask) != (y & mask):
                ans += 1
            mask <<= 1
        return ans