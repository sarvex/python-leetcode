class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """Two-pointer group comparison for character runs.

        Intuition:
            Compare consecutive groups of identical characters in both strings.
            Each group in typed must match the character and have at least as
            many repetitions as the corresponding group in name.

        Approach:
            1. Use two pointers to traverse both strings.
            2. At each position, verify characters match.
            3. Count the run length of each character group in both strings.
            4. Ensure typed's group length >= name's group length.
            5. Both pointers must reach the end simultaneously.

        Complexity:
            Time: O(m + n)
            Space: O(1)
        """
        name_len, typed_len = len(name), len(typed)
        name_idx = typed_idx = 0
        while name_idx < name_len and typed_idx < typed_len:
            if name[name_idx] != typed[typed_idx]:
                return False
            name_end = name_idx + 1
            while name_end < name_len and name[name_end] == name[name_idx]:
                name_end += 1
            typed_end = typed_idx + 1
            while typed_end < typed_len and typed[typed_end] == typed[typed_idx]:
                typed_end += 1
            if name_end - name_idx > typed_end - typed_idx:
                return False
            name_idx, typed_idx = name_end, typed_end
        return name_idx == name_len and typed_idx == typed_len
