from itertools import pairwise


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        """Generate all states by flipping consecutive '+' pairs to '-'.

        Intuition:
            Scan for adjacent '+' characters and produce a new string for each
            pair where both are flipped to '-'.

        Approach:
            1. Convert the string to a list for in-place modification.
            2. Use pairwise to find consecutive '+' pairs.
            3. For each pair, flip to '-', record the state, then flip back.

        Complexity:
            Time: O(n^2) due to string join for each valid pair
            Space: O(n) per generated state
        """
        characters = list(currentState)
        results: list[str] = []
        for i, (first, second) in enumerate(pairwise(characters)):
            if first == second == "+":
                characters[i] = characters[i + 1] = "-"
                results.append("".join(characters))
                characters[i] = characters[i + 1] = "+"
        return results
