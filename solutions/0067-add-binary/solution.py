# Iteration 3
# Source: https://www.geeksforgeeks.org/python/working-with-binary-data-in-python/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1. Convert a and b into decimal integers.
        # 2. Add a & b together.
        # 3. Convert the sum back to a binary string.
        # 4. Trim the str 2 chars to exclude '0b'.
        # 5. Return the sum.
        return bin(int(a, 2) + int(b, 2))[2:]

# Iteration 2
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a_index: int = len(a) - 1
#         b_index: int = len(b) - 1
#         carry: int = 0
#         sum: str = ""
#         while a_index >= 0 or b_index >= 0:
#             # Faster way of handling leading zeroes issue.
#             a_bit: int = int(a[a_index]) if a_index >= 0 else 0
#             b_bit: int = int(b[b_index]) if b_index >= 0 else 0
#             # Add the bits using XOR.
#             bit_sum: int = (carry ^ a_bit ^ b_bit)
#             sum = str(bit_sum) + sum
#             # Check if there are at least 2 1-bits from a_bit, b_bit, and carry
#             ab = a_bit & b_bit
#             ac = a_bit & carry
#             bc = b_bit & carry
#             carry = 1 if ab | ac | bc else 0
#             # Decrement indices
#             a_index -= 1
#             b_index -= 1
#         if carry:
#             sum = str(carry) + sum
#         return sum

# Iteration 1
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         padding_size: int = abs(len(a) - len(b))
#         # If padding size is 0, then a and b are the same length.
#         if padding_size > 0:
#             padding: str = "0" * padding_size
#             if len(a) > len(b):
#                 b = padding + b
#             else:
#                 a = padding + a
#         print(f"a = {a}, b = {b}")
#         sum: str = ""
#         carry: int = 0 # Carry over for algorithmic addition
#         for bit in range(len(a) - 1,-1,-1):
#             a_bit: int = int(a[bit])
#             b_bit: int = int(b[bit])
#             sum = str(carry ^ a_bit ^ b_bit) + sum
#             carry = 1 if [carry, a_bit, b_bit].count(1) > 1 else 0
#         if carry:
#             sum = str(carry) + sum
#         return sum
