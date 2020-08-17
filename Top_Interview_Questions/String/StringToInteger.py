class Solution:
    def myAtoi(self, str: str) -> int:
        res = ""
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        negative = False
        str = str.lstrip()
        if len(str) == 0:
            return 0
        if str[0] == '-':
            str = str[1:]
            negative = True
        elif str[0] == '+':
            str = str[1:]
        firstSpace = str.find(" ")
        if firstSpace != -1:
            str = str[:str.find(" ")]
        
        for i in range(len(str)):
            if str[i].isdigit():
                res += str[i]
            else:
                break
                
        if res == "":
            return 0
        if negative:
            res = -1 * int(res)
        else:
            res = int(res)
        
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res