class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """Find the sum of the first n positive k-mirror numbers.

        Incremental palindrome generation: Generate palindromes in base-k and check if they're also palindromes in base-10.

        Intuition:
        A k-mirror number is a number that is palindromic in both base-10 and base-k. To find these numbers,
        we can generate palindromes in base-k sequentially and check if they are also palindromes in base-10.

        Approach:
        1. Start with a small palindrome in base-k
        2. Generate the next palindrome in base-k
        3. Convert to base-10 and check if it's also a palindrome
        4. Repeat until we find n such numbers

        Complexity:
        Time: O(n * log(max_value)) where max_value is the nth k-mirror number
        Space: O(log(max_value)) for storing the palindrome digits
        """
        def _generate_next_palindrome(digits: list[str]) -> list[str]:
            """Generate the next palindrome in base-k from the current one."""
            mid = len(digits) // 2
            for i in range(mid, len(digits)):
                if int(digits[i]) + 1 < k:
                    # We can increment this digit and its mirror
                    digits[i] = digits[~i] = str(int(digits[i]) + 1)
                    # Reset all digits between the middle and current position
                    for j in range(mid, i):
                        digits[j] = digits[~j] = '0'
                    return digits
            # If we can't increment any digit, we need to add another digit
            return ["1"] + ["0"] * (len(digits) - 1) + ["1"]

        digits = ["0"]
        total_sum = 0
        count = 0

        while count < n:
            digits = _generate_next_palindrome(digits)
            base10_value = int("".join(digits), k)
            base10_str = str(base10_value)

            if base10_str == base10_str[::-1]:
                total_sum += base10_value
                count += 1

        return total_sum
