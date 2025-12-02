# Iteration 3
# Roman numerals map
roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Subtraction letters map
sub_map = {
    'IV': -1,
    'IX': -1,
    'XL': -10,
    'XC': -10,
    'CD': -100,
    'CM': -100
}

class Solution:
    def romanToInt(self, s: str) -> int:
        prev_letter: str = s[-1]
        integer: int = roman_map[prev_letter]
        index: int = len(s) - 2 # Start index second to last letter
        while index >= 0:
            current_letter: str = s[index]
            sub_val = sub_map.get(current_letter + prev_letter)
            if type(sub_val) is int:
                integer += sub_val
            else:
                integer += roman_map[current_letter]
            prev_letter = current_letter
            index -= 1
        return integer

# Iteration 2
# Roman numerals map
# roman_map = {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }

# # Subtraction letters map
# sub_map = {
#     'M': 'C',
#     'D': 'C',
#     'C': 'X',
#     'L': 'X',
#     'X': 'I',
#     'V': 'I',
# }

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         prev_letter: str | None = None # Instantiate previous letter for adding
#         index: int = 0 # Instantiate loop index
#         integer: int = 0 # Instantiate roman numeral integer
#         while index < len(s):
#             letter = s[index]
#             integer += roman_map[letter]
#             if letter != 'I' and (sub_letter := sub_map[letter]) == prev_letter:
#                 integer -= (roman_map[sub_letter] * 2)
#             prev_letter = s[index]
#             index += 1
#         return integer
        
# Iteration 1
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # Instantiate the Integer
#         integer: int = 0
#         # Helper function
#         def check_subtract(value: int, sub: int, prev_letter: str, check_letter: str) -> int:
#             """
#             Check letters are I, X, and C, the letters that can cause subtraction.
#             In the loop, the value will be added to the integer. However if the
#             check_letter occurs before the non-I letters, then we have to undo
#             the addition; this is solved by subtracting the double of the value.
#             """
#             return value - (sub * 2 if prev_letter == check_letter else 0)
#         # Iterate through the letters.
#         for i in range(len(s)):
#             letter = s[i]
#             prev_letter = s[i - 1] if i > 0 else None
#             match letter:
#                 case 'M':
#                     integer += check_subtract(1000, 100, prev_letter, 'C')
#                 case 'D':
#                     integer += check_subtract(500, 100, prev_letter, 'C')
#                 case 'C':
#                     integer += check_subtract(100, 10, prev_letter, 'X')
#                 case 'L':
#                     integer += check_subtract(50, 10, prev_letter, 'X')
#                 case 'X':
#                     integer += check_subtract(10, 1, prev_letter, 'I')
#                 case 'V':
#                     integer += check_subtract(5, 1, prev_letter, 'I')
#                 case _:
#                     integer += 1
#         return integer
