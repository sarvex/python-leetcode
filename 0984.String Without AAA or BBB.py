class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        """Greedy construction avoiding three consecutive identical characters.

        Intuition:
        Always place two of the more frequent character followed by one of the
        less frequent. When counts are equal, alternate single characters.
        This prevents three consecutive identical characters.

        Approach:
        1. While both a and b are positive, compare their counts
        2. If a > b: append "aab", if b > a: append "bba", if equal: append "ab"
        3. Append remaining characters of whichever is left

        Complexity:
        Time: O(a + b) for building the string
        Space: O(a + b) for the result
        """
        parts: list[str] = []
        while a and b:
            if a > b:
                parts.append("aab")
                a, b = a - 2, b - 1
            elif a < b:
                parts.append("bba")
                a, b = a - 1, b - 2
            else:
                parts.append("ab")
                a, b = a - 1, b - 1
        if a:
            parts.append("a" * a)
        if b:
            parts.append("b" * b)
        return "".join(parts)
