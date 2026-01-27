class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """Rotation check for k=1, full sort for k>=2.

        Intuition:
            With k=1, only rotations are possible, so find the lexicographically
            smallest rotation. With k>=2, any permutation is achievable via
            bubble-sort-like swaps, so just sort the string.

        Approach:
            1. If k == 1, try all rotations and return the smallest.
            2. If k >= 2, return the sorted string.

        Complexity:
            Time: O(n^2) for k=1, O(n log n) for k>=2.
            Space: O(n)
        """
        if k == 1:
            smallest = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                smallest = min(smallest, s)
            return smallest
        return "".join(sorted(s))
