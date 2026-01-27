class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        """Identify groups of 3+ consecutive identical characters.

        Intuition:
            Scan through the string tracking the start of each character group.
            When the group ends, check if its length is >= 3.

        Approach:
            1. Use two pointers to identify contiguous groups of the same character.
            2. If a group has length >= 3, record its start and end indices.

        Complexity:
            Time: O(n)
            Space: O(1) excluding output
        """
        start, length = 0, len(s)
        result: list[list[int]] = []
        while start < length:
            end = start
            while end < length and s[end] == s[start]:
                end += 1
            if end - start >= 3:
                result.append([start, end - 1])
            start = end
        return result
