class Solution:
    def largestPalindrome(self, n: int) -> int:
        """Construct palindromes from upper half and verify divisibility.

        Intuition:
            The largest palindrome product of two n-digit numbers can be
            found by constructing palindromes from the largest possible
            upper half downward and checking if any is a product of two
            n-digit numbers.

        Approach:
            Start from the maximum n-digit number and construct a palindrome
            by mirroring the upper half. Check if this palindrome is
            divisible by some n-digit number whose square is at least the
            palindrome.

        Complexity:
            Time: O(10^n) in the worst case
            Space: O(1)
        """
        max_val = 10**n - 1
        for upper in range(max_val, max_val // 10, -1):
            palindrome = remaining = upper
            while remaining:
                palindrome = palindrome * 10 + remaining % 10
                remaining //= 10
            divisor = max_val
            while divisor * divisor >= palindrome:
                if palindrome % divisor == 0:
                    return palindrome % 1337
                divisor -= 1
        return 9
