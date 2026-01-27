class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """Count substrings containing all three characters a, b, and c.

        Intuition:
            For each position, any substring starting at or before the earliest
            of the most recent occurrences of a, b, c and ending at the current
            position contains all three characters.

        Approach:
            Track the last seen index of each character. At each position, the
            number of valid substrings ending here equals min(last_a, last_b,
            last_c) + 1, since any start index from 0 to that minimum works.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        last_seen = {"a": -1, "b": -1, "c": -1}
        result = 0
        for i, char in enumerate(s):
            last_seen[char] = i
            result += min(last_seen["a"], last_seen["b"], last_seen["c"]) + 1
        return result
