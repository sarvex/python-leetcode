class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """Find all strings that are substrings of another string in the array.

        Intuition:
            For each word, check if it appears as a substring in any other word.

        Approach:
            Iterate through each word and check against all other words using
            the `in` operator for substring matching.

        Complexity:
            Time: O(n^2 * L) where L is the average word length
            Space: O(n) for the result list
        """
        result: list[str] = []
        for i, candidate in enumerate(words):
            if any(i != j and candidate in other for j, other in enumerate(words)):
                result.append(candidate)
        return result
