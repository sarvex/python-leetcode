class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        """Split a valid parentheses string to minimize the max nesting depth.

        Intuition:
            Assign parentheses at even depths to one group and odd depths to
            the other to balance the nesting evenly.

        Approach:
            Track the current depth. For opening brackets, assign based on the
            parity of the current depth before incrementing. For closing
            brackets, decrement first then assign based on parity.

        Complexity:
            Time: O(n) where n is the length of seq
            Space: O(n) for the result array
        """
        result = [0] * len(seq)
        depth = 0
        for i, char in enumerate(seq):
            if char == "(":
                result[i] = depth & 1
                depth += 1
            else:
                depth -= 1
                result[i] = depth & 1
        return result
