from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """Check if exactly one swap in s can produce goal.

        Intuition:
        Two strings are buddy strings if they differ in exactly two positions
        where the characters are swapped, or if they are identical and contain
        at least one duplicate character (allowing a no-op swap).

        Approach:
        1. Check length equality and character frequency match
        2. Count positions where characters differ
        3. Return True if diff == 2 (valid swap) or diff == 0 with duplicates

        Complexity:
        Time: O(n) where n is the string length
        Space: O(1) since alphabet size is fixed
        """
        if len(s) != len(goal):
            return False
        freq_s = Counter(s)
        freq_goal = Counter(goal)
        if freq_s != freq_goal:
            return False
        diff_count = sum(s[i] != goal[i] for i in range(len(s)))
        return diff_count == 2 or (
            diff_count == 0 and any(v > 1 for v in freq_s.values())
        )
