def plusOne(self, digits: List[int]) -> List[int]:
    if digits[len(digits)-1] != 9:
        digits[len(digits)-1] = digits[len(digits)-1] + 1
    else:
        digits[len(digits)-1] = 0
        carry_bit = 1
        for i in range(len(digits)-1):
            if (digits[len(digits)-i-2] + carry_bit) == 10:
                digits[len(digits)-i-2] = 0
                carry_bit = 1
            else:
                digits[len(digits)-i-2] = digits[len(digits)-i-2] + carry_bit
                carry_bit = 0
                break
        if carry_bit == 1:
            digits.insert(0,1)
    return digits