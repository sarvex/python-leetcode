from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        """Run-length encoding for string compression in-place.

        Intuition:
            Two-pointer approach to track character groups and write position,
            compressing by replacing consecutive characters with their count.

        Approach:
            1. Use three pointers: i (read), j (end of group), k (write)
            2. For each character, count consecutive occurrences
            3. Write the character followed by its count (if > 1)
            4. Continue until all characters are processed

        Complexity:
            Time: O(n) where n is the length of chars
            Space: O(1) as we modify the input array in-place
        """
        read_pos, write_pos, n = 0, 0, len(chars)

        while read_pos < n:
            # Find the end of current character group
            group_end = read_pos + 1
            while group_end < n and chars[group_end] == chars[read_pos]:
                group_end += 1

            # Write character
            chars[write_pos] = chars[read_pos]
            write_pos += 1

            # Write count if more than 1
            count = group_end - read_pos
            if count > 1:
                for digit in str(count):
                    chars[write_pos] = digit
                    write_pos += 1

            # Move to next character group
            read_pos = group_end

        return write_pos
