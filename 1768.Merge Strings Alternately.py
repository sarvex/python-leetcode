from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Two-pointer approach to merge strings alternately.

        Intuition:
        When merging two strings alternately, we can use zip_longest to pair characters
        from both strings, handling cases where one string is longer than the other.

        Approach:
        Use Python's zip_longest to pair characters from both strings, with empty string
        as the fillvalue for the shorter string. Then join these pairs together.

        Complexity:
        - Time: O(max(m, n)) where m and n are lengths of word1 and word2
        - Space: O(m + n) for the result string
        """
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

    def mergeAlternately_two_pointer(self, word1: str, word2: str) -> str:
        """Manual two-pointer approach to merge strings alternately.

        Intuition:
        We can manually track indices in both strings and append characters
        alternately until we exhaust both strings.

        Approach:
        Initialize two pointers, one for each string. While either pointer is within bounds,
        append characters from each string if available and increment the respective pointer.

        Complexity:
        - Time: O(max(m, n)) where m and n are lengths of word1 and word2
        - Space: O(m + n) for the result string
        """
        m, n = len(word1), len(word2)
        i = j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result.append(word1[i])
                i += 1
            if j < n:
                result.append(word2[j])
                j += 1

        return ''.join(result)
