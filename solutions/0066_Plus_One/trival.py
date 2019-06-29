class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, i = 1, len(digits) - 1
        while i >= 0:
            v = digits[i] + carry
            if v > 9:
                digits[i], carry = 0, 1
            else:
                digits[i], carry = v, 0
            if carry == 0:
                break
            i -= 1
        if carry == 1 and i < 0:
            digits.insert(0, 1)
        return digits
