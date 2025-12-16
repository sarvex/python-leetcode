from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)

        root_complexity = complexity[0]

        # If any computer i (i > 0) has complexity <= root,
        # it can never be unlocked because the chain must start at 0
        # and strictly increase in complexity.
        for i in range(1, n):
            if complexity[i] <= root_complexity:
                return 0

        # If all other computers have higher complexity than root,
        # then root (0) can directly unlock any of them.
        # Since 0 is always the first in the permutation,
        # the remaining n-1 computers can be arranged in any order.
        # So the answer is (n - 1)!

        result = 1
        for i in range(1, n):
            result = (result * i) % MOD

        return result
