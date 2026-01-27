from math import ceil


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """Repeated concatenation to find minimum repeats for substring match.

        Intuition:
            String b can only be a substring of repeated a if we repeat a
            enough times to cover b's length, plus at most 2 extra copies
            to handle alignment at boundaries.

        Approach:
            1. Start with ceil(len(b) / len(a)) copies of a.
            2. Check if b is a substring. If not, try up to 2 more copies.
            3. Return the count if found, otherwise -1.

        Complexity:
            Time: O(n * m) where n is len(a) and m is len(b) for substring check
            Space: O(n * repeats) for the concatenated string
        """
        len_a, len_b = len(a), len(b)
        repeats = ceil(len_b / len_a)
        repeated = [a] * repeats
        for _ in range(3):
            if b in "".join(repeated):
                return repeats
            repeats += 1
            repeated.append(a)
        return -1
