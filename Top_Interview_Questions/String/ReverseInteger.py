def reverse(self, x: int) -> int:
    # Trim rightmost zeroes
    if x == 0 or x > (pow(2,31)-1) or x < (pow(2,31) * (-1)):
        return 0
    negative = False
    if x < 0:
        x = x * (-1)
        negative = True
    # O(log x)
    while True:
        if (x % 10) == 0:
            x = int(x / 10)
        else:
            break
    # O(log x)
    l = []
    while True:
        if x >= 10:
            l.append(x%10)
            x = int(x / 10)
        else:
            l.append(x)
            break
    ans = 0
    # O(log x)
    for i in range(len(l)):
        ans += l[i] * pow(10, len(l) - 1 - i)
        
    if negative:
        ans = ans * (-1)
    if ans > (pow(2,31)-1) or ans < (pow(2,31) * (-1)):
        return 0
    return ans