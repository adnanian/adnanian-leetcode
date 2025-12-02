class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # Instantiate the list
        self_div_nums: List[int] = []
        # Loop from left to right.
        for n in range(left, right + 1, 1):
            # All single digits are self div nums.
            if n >= 1 and n <= 9:
                self_div_nums.append(n)
            # All multiples of 10 will not be self div nums,
            # because they have a 0 digit.
            elif n % 10 == 0:
                continue
            else:
                number_digits = n
                while number_digits > 0:
                    digit = number_digits % 10
                    # Self dividing number cannot have a 0 digit
                    # Self dividing number must be divisible by digit
                    if digit == 0 or n % digit != 0:
                        break
                    # Strip the right digit by dividing by 10.
                    number_digits //= 10
                if number_digits == 0:
                    self_div_nums.append(n)
        return self_div_nums
