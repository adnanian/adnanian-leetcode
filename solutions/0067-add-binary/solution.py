class Solution:
    def addBinary(self, a: str, b: str) -> str:
        padding_size: int = abs(len(a) - len(b))
        # If padding size is 0, then a and b are the same length.
        if padding_size > 0:
            padding: str = "0" * padding_size
            if len(a) > len(b):
                b = padding + b
            else:
                a = padding + a
        print(f"a = {a}, b = {b}")
        sum: str = ""
        carry: int = 0 # Carry over for algorithmic addition
        for digit in range(len(a) - 1,-1,-1):
            a_digit: int = int(a[digit])
            b_digit: int = int(b[digit])
            sum = str(carry ^ a_digit ^ b_digit) + sum
            carry = 1 if [carry, a_digit, b_digit].count(1) > 1 else 0
        if carry:
            sum = str(carry) + sum
        return sum
