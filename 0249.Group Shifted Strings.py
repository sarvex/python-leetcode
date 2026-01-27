from collections import defaultdict


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        """Group strings by normalized shift key using modular arithmetic.

        Intuition:
            Two strings belong to the same shift group if one can be shifted
            to become the other. Normalize each string by shifting so the
            first character becomes 'a'.

        Approach:
            For each string, compute a normalized form by shifting all
            characters so the first character maps to 'a'. Use modular
            arithmetic to wrap around. Group strings by their normalized key.

        Complexity:
            Time: O(n * k) where n is number of strings and k is max length
            Space: O(n * k) for the grouped output
        """
        groups = defaultdict(list)
        for string in strings:
            shift = ord(string[0]) - ord("a")
            normalized = []
            for char in string:
                shifted_char = ord(char) - shift
                if shifted_char < ord("a"):
                    shifted_char += 26
                normalized.append(chr(shifted_char))
            groups["".join(normalized)].append(string)
        return list(groups.values())
