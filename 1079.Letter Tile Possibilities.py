from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """Count distinct non-empty sequences from letter tiles.

        Intuition:
            Backtrack through all possible selections, using character counts
            to avoid duplicate sequences.

        Approach:
            Use a frequency counter. At each step, pick any available character,
            decrement its count, recurse, then restore. Each selection path
            represents a unique sequence.

        Complexity:
            Time: O(n!) in the worst case with all unique tiles
            Space: O(n) for recursion depth
        """

        def dfs(frequency: Counter) -> int:
            total = 0
            for char, count in frequency.items():
                if count > 0:
                    total += 1
                    frequency[char] -= 1
                    total += dfs(frequency)
                    frequency[char] += 1
            return total

        return dfs(Counter(tiles))
