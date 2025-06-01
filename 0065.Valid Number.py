class Solution:
    def isNumber(self, s: str) -> bool:
        """Validate if string is a valid number using state tracking approach.

        Intuition:
        Parse the string character by character while tracking the presence of
        decimal point and exponent. Handle edge cases like signs and ensure
        proper numeric format throughout.

        Approach:
        1. Skip leading sign if present
        2. Check for empty string after sign
        3. Handle special case for decimal point
        4. Iterate through remaining characters tracking decimal points and exponents
        5. Validate proper format for exponents including signs
        6. Ensure all other characters are numeric

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(1) using constant extra space
        """
        n = len(s)
        i = 0

        # Handle leading sign
        if i < n and s[i] in '+-':
            i += 1

        # Empty string or just a sign
        if i == n:
            return False

        # Special case: decimal point followed by exponent or end of string
        if s[i] == '.' and (i + 1 == n or s[i + 1] in 'eE'):
            return False

        # Track decimal point and exponent
        has_decimal = has_exponent = False
        j = i

        while j < n:
            match s[j]:
                case '.':
                    # Decimal point after exponent or second decimal point
                    if has_exponent or has_decimal:
                        return False
                    has_decimal = True

                case 'e' | 'E':
                    # Invalid exponent: already has one, at beginning, or at end
                    if has_exponent or j == i or j == n - 1:
                        return False
                    has_exponent = True

                    # Handle sign after exponent
                    if j + 1 < n and s[j + 1] in '+-':
                        j += 1
                        if j == n - 1:  # Sign at the end is invalid
                            return False

                case c if not c.isdigit():
                    # Non-numeric character
                    return False

            j += 1

        return True
