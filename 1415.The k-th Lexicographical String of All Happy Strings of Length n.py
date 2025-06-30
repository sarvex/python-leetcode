class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Mathematical approach to find k-th happy string without generating all strings.

        Intuition:
        A happy string has no adjacent identical characters. For the first character,
        we have 3 choices (a, b, c). For each subsequent character, we have 2 choices
        (any letter except the previous one). So total count is 3 * 2^(n-1).

        Approach:
        1. Check if k is valid (k <= 3 * 2^(n-1))
        2. For each position, determine the character based on k
        3. Update k for the next position

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(n) for the result string
        """
        # Calculate total possible happy strings
        total = 3 * (1 << (n - 1)) if n > 0 else 0

        # If k is out of range, return empty string
        if k > total:
            return ""

        # Adjust k to be 0-indexed for calculations
        k -= 1

        # Initialize result with first character
        choices_per_first_char = total // 3
        first_char = chr(ord('a') + (k // choices_per_first_char))
        result = [first_char]

        # Update k for remaining positions
        k %= choices_per_first_char

        # Fill remaining positions
        for i in range(1, n):
            # For each position after first, we have 2 choices
            choices_per_char = 1 << (n - i - 1)

            # Determine which of the 2 valid characters to use
            valid_chars = [c for c in ['a', 'b', 'c'] if c != result[-1]]
            next_char = valid_chars[k // choices_per_char]
            result.append(next_char)

            # Update k for next position
            k %= choices_per_char

        return ''.join(result)
