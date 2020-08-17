class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = "1"
        for iteration in range(n-1):
            res = ""
            value = s[0]
            frequency = 1
            for idx in range(1, len(s)):
                if s[idx] == value:
                    frequency += 1
                else:
                    res = res + str(frequency) + value
                    value = s[idx]
                    frequency = 1
            s = res + str(frequency) + value
        return s