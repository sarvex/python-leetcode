from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """Count bulls (exact matches) and cows (misplaced matches) using frequency counters.

        Intuition:
            Bulls are digits matching in both value and position. Cows are digits
            matching in value but not position, counted from the remaining
            non-bull digits using frequency overlap.

        Approach:
            1. Iterate through both strings simultaneously.
            2. Count bulls where characters match at the same position.
            3. For non-matching positions, accumulate character frequencies separately.
            4. Cows are the sum of minimum overlapping frequencies.

        Complexity:
            Time: O(n) where n is the length of the strings
            Space: O(1) since digit alphabet is fixed size 10
        """
        secret_counts: Counter[str] = Counter()
        guess_counts: Counter[str] = Counter()
        bulls = 0
        for secret_char, guess_char in zip(secret, guess):
            if secret_char == guess_char:
                bulls += 1
            else:
                secret_counts[secret_char] += 1
                guess_counts[guess_char] += 1
        cows = sum(
            min(secret_counts[char], guess_counts[char]) for char in secret_counts
        )
        return f"{bulls}A{cows}B"
