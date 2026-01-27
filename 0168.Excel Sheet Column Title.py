class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """Base-26 Conversion with 1-Based Indexing.

        Intuition:
            Excel column titles are essentially a base-26 numeral system but
            with 1-based indexing (A=1, Z=26) instead of 0-based.

        Approach:
            Repeatedly subtract 1 to convert from 1-based to 0-based indexing,
            then take modulo 26 to get the current character. Divide by 26 to
            process the next digit. Build the result in reverse order.

        Complexity:
            Time: O(log_26(n)) number of digits in base-26 representation
            Space: O(log_26(n)) for the result characters
        """
        result: list[str] = []
        while columnNumber:
            columnNumber -= 1
            result.append(chr(ord("A") + columnNumber % 26))
            columnNumber //= 26
        return "".join(result[::-1])
