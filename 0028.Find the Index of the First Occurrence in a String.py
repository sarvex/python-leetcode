class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        String Matching with Sliding Window

        Intuition:
        The simplest approach is to check each possible substring of haystack
        with the same length as needle and see if it matches needle.

        Approach:
        1. Get the lengths of both strings
        2. If needle is empty, return 0 (first occurrence is at index 0)
        3. Iterate through haystack with a sliding window of size equal to needle's length
        4. For each position, check if the substring matches needle
        5. If a match is found, return the starting index
        6. If no match is found after checking all positions, return -1

        Complexity:
        Time: O(n * m) where n is the length of haystack and m is the length of needle
        Space: O(1) as we only use constant extra space
        """
        n, m = len(haystack), len(needle)

        # Edge case: empty needle
        if m == 0:
            return 0

        # Sliding window approach
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1

    def strStr_kmp(self, haystack: str, needle: str) -> int:
        """
        String Matching with KMP Algorithm

        Intuition:
        The Knuth-Morris-Pratt (KMP) algorithm avoids unnecessary comparisons
        by using a prefix function to skip ahead when a mismatch occurs.

        Approach:
        1. Build the KMP prefix table for the needle
        2. Use the table to efficiently search for needle in haystack
        3. When a mismatch occurs, use the prefix table to determine how much
           to shift the pattern rather than starting over

        Complexity:
        Time: O(n + m) where n is the length of haystack and m is the length of needle
        Space: O(m) for storing the prefix table
        """
        if not needle:
            return 0

        # Build KMP prefix table
        def build_prefix_table(pattern: str) -> list[int]:
            m = len(pattern)
            prefix = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = prefix[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1

                prefix[i] = j

            return prefix

        # KMP search
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        prefix = build_prefix_table(needle)
        j = 0  # Position in needle

        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = prefix[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == m:
                return i - m + 1

        return -1
