class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """Check if all binary codes of length k appear as substrings.

        Intuition:
            Collect all distinct substrings of length k and verify their count
            equals 2^k.

        Approach:
            Use a set comprehension to gather all substrings of length k,
            then check if the set size equals 2^k.

        Complexity:
            Time: O(n * k) for substring extraction
            Space: O(2^k * k) for storing substrings
        """
        substrings = {s[i : i + k] for i in range(len(s) - k + 1)}
        return len(substrings) == 1 << k
