class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        start = 0
        end = 0
        for i in range(n):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            maxlen = max(len1, len2)
            if maxlen > (end - start + 1):
                start = i - int(maxlen/2) + (maxlen % 2 == 0)
                end = i + int(maxlen/2)
        return s[start:end+1]
    def expand(self, s: str, left: int, right: int) -> int:
        length = 0
        while right < len(s):
            if s[left] == s[right]:
                length = right - left + 1
                left -= 1
                right += 1
            else:
                return right - left - 1
            if left < 0 or right >= len(s):
                break
        return length