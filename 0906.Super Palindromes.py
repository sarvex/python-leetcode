palindrome_roots = []
for _i in range(1, 10**5 + 1):
    _s = str(_i)
    _odd_palindrome = _s[::-1]
    _even_palindrome = _s[:-1][::-1]
    palindrome_roots.append(int(_s + _odd_palindrome))
    palindrome_roots.append(int(_s + _even_palindrome))


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """Enumerate palindrome roots and check if their squares are palindromes.

        Intuition:
            A super palindrome is a palindrome whose square root is also a
            palindrome. We can enumerate all palindromic roots up to a limit
            and check if their squares fall within the range and are palindromes.

        Approach:
            1. Precompute all palindrome numbers up to ~10^5 digits by
               mirroring digit strings (both odd and even length).
            2. For each palindrome root, compute its square.
            3. Check if the square is within [left, right] and is a palindrome.

        Complexity:
            Time: O(W^(1/4) * log(W)) where W is the upper bound
            Space: O(W^(1/4))
        """

        def is_palindrome(number: int) -> bool:
            reversed_num, temp = 0, number
            while temp:
                reversed_num = reversed_num * 10 + temp % 10
                temp //= 10
            return number == reversed_num

        lower, upper = int(left), int(right)
        return sum(
            lower <= squared <= upper and is_palindrome(squared)
            for squared in map(lambda root: root * root, palindrome_roots)
        )
