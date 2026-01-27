class Solution:
    def reformat(self, s: str) -> str:
        """Reformat string by alternating letters and digits.

        Intuition:
            Separate letters and digits, then interleave them. This is only
            possible if their counts differ by at most 1.

        Approach:
            Split into letters and digits. Ensure the longer group comes
            first. Interleave pairs and append the remaining character
            from the longer group if needed.

        Complexity:
            Time: O(n) for splitting and interleaving
            Space: O(n) for the result
        """
        letters = [ch for ch in s if ch.islower()]
        digits = [ch for ch in s if ch.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(letters) < len(digits):
            letters, digits = digits, letters
        result: list[str] = []
        for letter, digit in zip(letters, digits):
            result.append(letter + digit)
        if len(letters) > len(digits):
            result.append(letters[-1])
        return "".join(result)
