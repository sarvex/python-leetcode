class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        """Hash set lookup after computing the required swap difference.

        Intuition:
            If Alice gives box of size a and receives size b, then
            sum_alice - a + b = sum_bob - b + a, so b = a - diff/2.
            Look up the required b in a set of Bob's sizes.

        Approach:
            1. Compute the difference between Alice's and Bob's total candies.
            2. For each of Alice's boxes, compute the required Bob box size.
            3. Check existence in a set built from Bob's sizes.

        Complexity:
            Time: O(n + m)
            Space: O(m)
        """
        difference = (sum(aliceSizes) - sum(bobSizes)) >> 1
        bob_set = set(bobSizes)
        for alice_box in aliceSizes:
            target_bob_box = alice_box - difference
            if target_bob_box in bob_set:
                return [alice_box, target_bob_box]
