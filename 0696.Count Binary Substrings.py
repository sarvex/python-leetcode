class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """Group consecutive characters and count valid adjacent pairs.

        Intuition:
            Valid substrings have equal numbers of consecutive 0s and 1s.
            Grouping consecutive identical characters lets us count valid
            substrings as the minimum of adjacent group sizes.

        Approach:
            1. Group consecutive identical characters and record group sizes.
            2. For each pair of adjacent groups, the number of valid substrings
               is the minimum of their sizes.
            3. Sum all such minimums.

        Complexity:
            Time: O(n) single pass to group and count
            Space: O(n) for the groups array in the worst case
        """
        index, length = 0, len(s)
        groups: list[int] = []
        while index < length:
            count = 1
            while index + 1 < length and s[index + 1] == s[index]:
                count += 1
                index += 1
            groups.append(count)
            index += 1
        total = 0
        for i in range(1, len(groups)):
            total += min(groups[i - 1], groups[i])
        return total
