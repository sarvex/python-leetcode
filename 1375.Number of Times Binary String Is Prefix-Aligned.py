class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        """Count how many times the binary string is prefix-aligned after each flip.

        Intuition:
            The string is prefix-aligned when all flipped bits form a
            contiguous prefix, which happens exactly when the maximum flipped
            position equals the current step number.

        Approach:
            Track the running maximum of flipped positions. After each flip,
            if the maximum equals the step number (1-indexed), all bits up to
            that point have been flipped, forming a valid prefix.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        result = 0
        max_flipped = 0
        for step, position in enumerate(flips, 1):
            max_flipped = max(max_flipped, position)
            result += max_flipped == step
        return result
