class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Bidirectional character mapping to verify isomorphism.

        Intuition:
            Two strings are isomorphic if there is a one-to-one mapping between
            characters. We need to check both directions to ensure no two
            characters map to the same target.

        Approach:
            1. Maintain two dictionaries for forward (s->t) and reverse (t->s)
               mappings.
            2. For each character pair, verify consistency with existing
               mappings.
            3. Return False on any conflict, True if all pairs are consistent.

        Complexity:
            Time: O(n)
            Space: O(n) for the mapping dictionaries
        """
        forward_map = {}
        reverse_map = {}
        for char_s, char_t in zip(s, t):
            if (char_s in forward_map and forward_map[char_s] != char_t) or (
                char_t in reverse_map and reverse_map[char_t] != char_s
            ):
                return False
            forward_map[char_s] = char_t
            reverse_map[char_t] = char_s
        return True
