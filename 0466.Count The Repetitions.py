class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """Precompute s2 traversal counts per starting index in s1.

        Intuition:
            For each starting position in s2, simulate one full pass of s1
            to determine how many complete s2 cycles occur and the ending
            position. Then replay n1 copies of s1 using those precomputed
            mappings.

        Approach:
            Build a dictionary mapping each starting index in s2 to the
            number of complete s2 matches and the ending index after one
            pass through s1. Iterate n1 times, accumulating the total s2
            count, and divide by n2.

        Complexity:
            Time: O(len(s2) * len(s1) + n1)
            Space: O(len(s2))
        """
        s2_len = len(s2)
        traversal_map: dict[int, tuple[int, int]] = {}
        for start in range(s2_len):
            count = 0
            pos = start
            for char in s1:
                if char == s2[pos]:
                    pos += 1
                if pos == s2_len:
                    count += 1
                    pos = 0
            traversal_map[start] = (count, pos)

        total_count = 0
        pos = 0
        for _ in range(n1):
            count, pos = traversal_map[pos]
            total_count += count
        return total_count // n2
