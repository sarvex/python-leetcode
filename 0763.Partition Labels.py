class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """Greedy partitioning using last occurrence of each character.

        Intuition:
            A partition must extend at least to the last occurrence of every
            character it contains. Track the farthest required endpoint and
            cut when the current index reaches it.

        Approach:
            1. Record the last index of each character.
            2. Sweep left to right, expanding the current partition's end to
               the max last-occurrence of characters seen so far.
            3. When the current index equals the partition end, finalize the part.

        Complexity:
            Time: O(N)
            Space: O(1) — at most 26 entries
        """
        last_occurrence = {ch: i for i, ch in enumerate(s)}
        partition_end = partition_start = 0
        result: list[int] = []
        for i, ch in enumerate(s):
            partition_end = max(partition_end, last_occurrence[ch])
            if partition_end == i:
                result.append(i - partition_start + 1)
                partition_start = i + 1
        return result
