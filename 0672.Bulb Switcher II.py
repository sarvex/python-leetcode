class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        """Enumerate all button combinations using bitmask to count unique states.

        Intuition:
        There are only 4 operations and the pattern repeats every 6 bulbs. Enumerate
        all subsets of operations with valid press counts and track unique states.

        Approach:
        1. Define 4 operation masks (all, odd, even, every-third).
        2. Enumerate all 16 subsets of the 4 operations.
        3. Filter subsets where the count has the same parity as presses and count <= presses.
        4. Apply selected operations via XOR and normalize to first n bulbs (max 6).
        5. Count unique resulting states.

        Complexity:
        Time: O(1) - fixed number of operations
        Space: O(1)
        """
        ops = (0b111111, 0b010101, 0b101010, 0b100100)
        n = min(n, 6)
        unique_states = set()
        for mask in range(1 << 4):
            button_count = mask.bit_count()
            if button_count <= presses and button_count % 2 == presses % 2:
                state = 0
                for i, op in enumerate(ops):
                    if (mask >> i) & 1:
                        state ^= op
                state &= (1 << 6) - 1
                state >>= 6 - n
                unique_states.add(state)
        return len(unique_states)
