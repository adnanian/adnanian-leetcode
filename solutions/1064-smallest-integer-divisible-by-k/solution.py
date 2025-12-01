class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # All negatives, even numbers, and multiples
        # of 5 will return -1 since it's impossible
        # to have a smallest number where n is divisible
        # by k and only contains the digit 1.
        if k % 2 == 0 or k % 5 == 0 or k < 1 or k > 100000:
            return -1
        # Solution: start n at one, then add a digit each
        # iteration until n % k == 0
        # To add a digit, multiply by 10, then add 1.
        n: int = 1
        length_of_n = 1
        while (n % k != 0):
            n = (n * 10) + 1
            length_of_n += 1
        # Return the length of n
        return length_of_n
