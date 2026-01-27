from collections import defaultdict
from functools import cache
from itertools import pairwise, product


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        """DFS with memoization to check if a valid pyramid can be built.

        Intuition:
            Each adjacent pair in the current row determines possible characters
            for the row above. Enumerate all valid next rows recursively.

        Approach:
            1. Build a lookup mapping each (left, right) pair to allowed top chars.
            2. For each row, collect possible characters for each position.
            3. Use product to enumerate all valid next rows; recurse until
               a single character row is reached.

        Complexity:
            Time: O(A^N) worst case where A = alphabet size, N = bottom length
            Space: O(N^2) for memoization
        """

        @cache
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            candidates = []
            for left, right in pairwise(row):
                options = char_map[left, right]
                if not options:
                    return False
                candidates.append(options)
            return any(dfs("".join(next_row)) for next_row in product(*candidates))

        char_map: dict[tuple[str, str], list[str]] = defaultdict(list)
        for left, right, top in allowed:
            char_map[left, right].append(top)
        return dfs(bottom)
