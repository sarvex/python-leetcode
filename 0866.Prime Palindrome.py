class Solution:
    def primePalindrome(self, n: int) -> int:
        """Linear scan with palindrome check and primality test, skipping even-length palindromes.

        Intuition:
        All even-length palindromes are divisible by 11 (except 11 itself),
        so we can skip the range (10^7, 10^8) entirely. Check each candidate
        for being both a palindrome and prime.

        Approach:
        1. For each candidate starting from n, check if it is a palindrome
        2. If palindrome, test primality by trial division
        3. Skip 8-digit numbers since even-length palindromes > 11 are not prime

        Complexity:
        Time: O(n^0.5) per primality check, overall depends on prime gaps
        Space: O(1)
        """

        def is_prime(number: int) -> bool:
            if number < 2:
                return False
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    return False
                divisor += 1
            return True

        def reverse_number(number: int) -> int:
            reversed_val = 0
            while number:
                reversed_val = reversed_val * 10 + number % 10
                number //= 10
            return reversed_val

        while True:
            if reverse_number(n) == n and is_prime(n):
                return n
            if 10**7 < n < 10**8:
                n = 10**8
            n += 1
