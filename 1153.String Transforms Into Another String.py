class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """Check if str1 can be converted to str2 via character mapping.

        Intuition:
            Each character in str1 must map consistently to a character in str2.
            If str2 uses all 26 characters, no temporary character is available
            for intermediate conversions.

        Approach:
            If strings are equal, return True. If str2 uses all 26 letters,
            return False (no spare character for swapping). Otherwise verify
            each character in str1 maps to exactly one character in str2.

        Complexity:
            Time: O(n)
            Space: O(1) — at most 26 mappings
        """
        if str1 == str2:
            return True
        if len(set(str2)) == 26:
            return False
        mapping: dict[str, str] = {}
        for source_char, target_char in zip(str1, str2):
            if source_char not in mapping:
                mapping[source_char] = target_char
            elif mapping[source_char] != target_char:
                return False
        return True
