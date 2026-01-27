class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """Reverse every first k characters in each 2k-length segment.

        Intuition:
            Process the string in chunks of 2k. For each chunk, reverse the
            first k characters and leave the rest unchanged.

        Approach:
            Convert to list. Iterate with step 2k, reversing the slice
            [i:i+k] at each step.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        chars = list(s)
        for i in range(0, len(chars), 2 * k):
            chars[i : i + k] = reversed(chars[i : i + k])
        return "".join(chars)
