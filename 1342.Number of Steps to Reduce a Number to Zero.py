class Solution:
    def numberOfSteps(self, num: int) -> int:
        """Count steps to reduce a number to zero by subtracting 1 (odd) or dividing by 2 (even).

        Intuition:
            Simulate the process: if odd subtract 1, if even right-shift by 1.

        Approach:
            Loop while num is nonzero, applying the appropriate operation each
            step and counting iterations.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        steps = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps
