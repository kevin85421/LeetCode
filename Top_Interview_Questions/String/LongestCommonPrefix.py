class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        common_prefix = ""
        current_char = ""
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for str in strs:
                if i > (len(str)-1) or str[i] != current_char:
                    return common_prefix
            common_prefix += current_char
        return common_prefix