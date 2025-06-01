from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Horizontal scanning approach to find the longest common prefix.

        Intuition:
        Compare characters at the same position across all strings until we find a mismatch.

        Approach:
        1. Handle edge cases: empty list or empty first string
        2. Iterate through each character of the first string
        3. For each character, check if it matches the same position in all other strings
        4. If a mismatch is found or we reach the end of any string, return the prefix so far

        Complexity:
        Time: O(S) where S is the sum of all characters in all strings
        Space: O(1) as we only use constant extra space
        """
        # Handle edge cases
        if not strs:
            return ""

        if not strs[0]:
            return ""

        # Get the first string as our reference
        first_str = strs[0]

        # Iterate through each character of the first string
        for i in range(len(first_str)):
            # Check this character against all other strings
            for s in strs[1:]:
                # If we've reached the end of current string or found a mismatch
                if i >= len(s) or s[i] != first_str[i]:
                    return first_str[:i]

        # If we get here, the entire first string is a prefix of all strings
        return first_str
