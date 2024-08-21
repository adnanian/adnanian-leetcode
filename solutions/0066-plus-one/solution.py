class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_index = len(digits) - 1
        carry = True
        while (carry and digit_index >= 0):
            if digits[digit_index] == 9:
                digits[digit_index] = 0
                if digit_index == 0:
                    digits.insert(0, 0)
                    digit_index += 1
            else:
                digits[digit_index] += 1
                carry = False
            # print(f"{digits} - {digit_index}")
            digit_index -= 1
            
        return digits
            
