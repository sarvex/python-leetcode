class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """Two Pointer Parsing.

        Intuition:
            Parse version numbers segment by segment, comparing each numeric
            revision level without splitting into arrays.

        Approach:
            Use two pointers to traverse both version strings simultaneously.
            For each segment (delimited by dots), accumulate the numeric value
            character by character. Compare the two values and return -1 or 1
            if they differ. If all segments are equal, return 0.

        Complexity:
            Time: O(max(m, n)) where m and n are the string lengths
            Space: O(1) constant extra space
        """
        len1, len2 = len(version1), len(version2)
        i = j = 0
        while i < len1 or j < len2:
            revision1 = revision2 = 0
            while i < len1 and version1[i] != ".":
                revision1 = revision1 * 10 + int(version1[i])
                i += 1
            while j < len2 and version2[j] != ".":
                revision2 = revision2 * 10 + int(version2[j])
                j += 1
            if revision1 != revision2:
                return -1 if revision1 < revision2 else 1
            i, j = i + 1, j + 1
        return 0
