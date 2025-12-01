class Solution:
    def isUgly(self, n: int) -> bool:
        # This is a beautiful number to me.
        # How can anybody call this ugly?
        # All non-positive numbers must return false.
        if n < 1:
            return False
        # For numbers 1 to 6, they are all ugly numbers.
        if n >= 1 and n <= 6:
            return True
        # For numbers 7 and above, they are not ugly if they are not divisible by 2, 3, or 5.
        # Searching for other primes involves prime factorization, which will therefore involve recursion.
        ugly_primes: List[int] = [2, 3, 5]
        for prime in ugly_primes:
            if (int_quotient := n // prime) == n / prime:
                if self.isUgly(int_quotient):
                    return True
        return False
        
        
