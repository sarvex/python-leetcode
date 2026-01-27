class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        """Validate UTF-8 encoding using bit pattern matching.

        Intuition:
            UTF-8 has specific bit patterns for leading and continuation
            bytes. We can validate by checking each byte's high bits and
            counting expected continuation bytes.

        Approach:
            1. Track the number of expected continuation bytes.
            2. For each byte, if continuation bytes are expected, verify
               it starts with 10xxxxxx.
            3. Otherwise, determine the character length from the leading
               byte's bit pattern (0xxxxxxx, 110xxxxx, 1110xxxx, 11110xxx).
            4. Return True if all bytes are consumed with no pending continuations.

        Complexity:
            Time: O(n) where n is the length of data
            Space: O(1)
        """
        continuation_count = 0
        for value in data:
            if continuation_count > 0:
                if value >> 6 != 0b10:
                    return False
                continuation_count -= 1
            elif value >> 7 == 0:
                continuation_count = 0
            elif value >> 5 == 0b110:
                continuation_count = 1
            elif value >> 4 == 0b1110:
                continuation_count = 2
            elif value >> 3 == 0b11110:
                continuation_count = 3
            else:
                return False
        return continuation_count == 0
