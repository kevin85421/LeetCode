class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1,2]
        if n <= len(l):
            return l[n-1]
        for i in range(n - len(l) - 1):
            l[i%2] = l[0] + l[1]
        return l[0] + l[1]