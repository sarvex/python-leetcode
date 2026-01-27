from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        """Count valid words for each puzzle using bitmask enumeration.

        Intuition:
            A word is valid for a puzzle if it contains the puzzle's first letter
            and all its letters are in the puzzle. Bitmasks efficiently represent
            character sets.

        Approach:
            Convert each word to a bitmask and count frequencies. For each puzzle,
            enumerate all submasks of the puzzle's bitmask that include the first
            letter, summing up matching word counts.

        Complexity:
            Time: O(W * L + P * 2^7) where W=words, P=puzzles, L=avg word length
            Space: O(W) for the bitmask counter
        """
        bitmask_count: Counter[int] = Counter()
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord("a"))
            bitmask_count[mask] += 1

        result: list[int] = []
        for puzzle in puzzles:
            puzzle_mask = 0
            for ch in puzzle:
                puzzle_mask |= 1 << (ord(ch) - ord("a"))
            first_bit = ord(puzzle[0]) - ord("a")
            valid_count = 0
            submask = puzzle_mask
            while submask:
                if submask >> first_bit & 1:
                    valid_count += bitmask_count[submask]
                submask = (submask - 1) & puzzle_mask
            result.append(valid_count)
        return result
