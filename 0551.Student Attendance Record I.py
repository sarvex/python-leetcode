class Solution:
    def checkRecord(self, s: str) -> bool:
        """Check attendance eligibility by counting absences and consecutive lates.

        Intuition:
            A student is eligible if they have fewer than 2 absences and never
            have 3 or more consecutive late days.

        Approach:
            1. Count occurrences of 'A' and check if less than 2.
            2. Check that 'LLL' does not appear as a substring.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return s.count("A") < 2 and "LLL" not in s
