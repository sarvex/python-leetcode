class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """Minimum swaps to make two strings equal by counting mismatches.

        Intuition:
            Mismatches come in two types: positions where s1 has 'x' and s2 has 'y'
            (xy-type), and vice versa (yx-type). Two same-type mismatches can be
            resolved with one swap; two different-type mismatches need two swaps.

        Approach:
            Count xy and yx mismatches. If their sum is odd, it is impossible.
            Otherwise, pair same-type mismatches first (each costs 1 swap), then
            handle remaining cross-type pairs (each costs 2 swaps).

        Complexity:
            Time: O(n) — single pass through both strings
            Space: O(1) — only two counters
        """
        xy_count = yx_count = 0
        for char_a, char_b in zip(s1, s2):
            xy_count += char_a < char_b
            yx_count += char_a > char_b
        if (xy_count + yx_count) % 2:
            return -1
        return xy_count // 2 + yx_count // 2 + xy_count % 2 + yx_count % 2
