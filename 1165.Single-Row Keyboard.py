class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """Calculate total finger movement time on a single-row keyboard.

        Intuition:
            The finger moves from one key position to the next. Total time is
            the sum of absolute differences between consecutive key positions.

        Approach:
            Build a position map for each character on the keyboard. Iterate
            through the word, summing absolute position differences from the
            current finger position.

        Complexity:
            Time: O(n) where n is the length of word
            Space: O(1) — position map has at most 26 entries
        """
        position = {char: idx for idx, char in enumerate(keyboard)}
        total_time = 0
        current_pos = 0
        for char in word:
            total_time += abs(position[char] - current_pos)
            current_pos = position[char]
        return total_time
