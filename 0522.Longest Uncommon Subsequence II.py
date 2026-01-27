class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        """Check each string as candidate for longest uncommon subsequence.

        Intuition:
            A string is an uncommon subsequence if it is not a subsequence of
            any other string in the list. Check each string against all others.

        Approach:
            For each string, verify it is not a subsequence of any other string.
            If it passes, consider its length as a candidate answer.

        Complexity:
            Time: O(n^2 * k) where k is max string length
            Space: O(1)
        """

        def is_subsequence(source: str, target: str) -> bool:
            i = j = 0
            while i < len(source) and j < len(target):
                if source[i] == target[j]:
                    i += 1
                j += 1
            return i == len(source)

        result = -1
        for i, candidate in enumerate(strs):
            for j, other in enumerate(strs):
                if i != j and is_subsequence(candidate, other):
                    break
            else:
                result = max(result, len(candidate))
        return result
