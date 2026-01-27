class Solution:
    def beforeAndAfterPuzzles(self, phrases: list[str]) -> list[str]:
        """Generate before-and-after puzzles from phrases.

        Intuition:
            Two phrases can merge when the last word of the first matches the
            first word of the second, forming a combined phrase.

        Approach:
            Extract the first and last word of each phrase. For every pair (i, j)
            where i != j and last word of i equals first word of j, concatenate
            phrase i with the remainder of phrase j. Return sorted unique results.

        Complexity:
            Time: O(n^2 * L) where L is average phrase length
            Space: O(n^2) for results in worst case
        """
        word_boundaries: list[tuple[str, str]] = []
        for phrase in phrases:
            tokens = phrase.split()
            word_boundaries.append((tokens[0], tokens[-1]))

        phrase_count = len(word_boundaries)
        merged: list[str] = []
        for i in range(phrase_count):
            for j in range(phrase_count):
                if i != j and word_boundaries[i][1] == word_boundaries[j][0]:
                    merged.append(phrases[i] + phrases[j][len(word_boundaries[j][0]) :])

        return sorted(set(merged))
