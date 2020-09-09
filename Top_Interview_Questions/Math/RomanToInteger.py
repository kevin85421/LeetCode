class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        length = len(s)
        max_char = s[length-1]
        ans = 0
        for i in range(length):
            index = length - 1 - i
            if roman_dict[max_char] > roman_dict[s[index]]:
                ans -= roman_dict[s[index]]
                continue
            ans += roman_dict[s[index]]
            max_char = s[index]
        return ans