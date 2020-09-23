class Solution:
    def hammingWeight(self, n: int) -> int:
        n2str = bin(n)[2:]
        ans = 0
        for ch in n2str:
            if ch == '1':
                ans += 1
        return ans