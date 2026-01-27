class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """Check rotation by concatenation containment.

        Intuition:
            If goal is a rotation of s, then goal must appear as a substring
            of s concatenated with itself.

        Approach:
            1. Check lengths are equal.
            2. Check if goal is a substring of s + s.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        return len(s) == len(goal) and goal in s + s
