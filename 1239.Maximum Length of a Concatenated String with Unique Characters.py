class Solution:
    def maxLength(self, arr: list[str]) -> int:
        """Find maximum length of concatenation with all unique characters.

        Intuition:
            Represent each string as a bitmask of its characters. Only strings
            with all unique characters (no duplicate within themselves) are
            candidates. Incrementally build valid combinations.

        Approach:
            For each string, compute its character bitmask. Skip strings with
            duplicate characters. Maintain a list of valid combined masks.
            For each new valid string, try combining it with every existing
            mask where there is no character overlap.

        Complexity:
            Time: O(2^n * 26) where n is the number of valid strings
            Space: O(2^n)
        """
        max_length = 0
        masks: list[int] = [0]
        for string in arr:
            mask = 0
            for char in string:
                bit = ord(char) - ord("a")
                if mask >> bit & 1:
                    mask = 0
                    break
                mask |= 1 << bit
            if mask == 0:
                continue
            for existing_mask in masks:
                if existing_mask & mask == 0:
                    masks.append(existing_mask | mask)
                    max_length = max(max_length, (existing_mask | mask).bit_count())
        return max_length
