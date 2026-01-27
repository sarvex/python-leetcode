from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        """Find lexicographically smallest string after allowed swaps using union-find.

        Intuition:
            Indices connected by swap pairs form groups. Within each group,
            characters can be freely rearranged, so sort them for the smallest result.

        Approach:
            Use union-find to group connected indices. Collect characters per
            group, sort them in reverse, and pop the smallest character for
            each position in order.

        Complexity:
            Time: O(n log n * α(n)) where α is inverse Ackermann
            Space: O(n)
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        length = len(s)
        parent = list(range(length))
        for idx_a, idx_b in pairs:
            parent[find(idx_a)] = find(idx_b)
        group_chars: dict[int, list[str]] = defaultdict(list)
        for i, char in enumerate(s):
            group_chars[find(i)].append(char)
        for root in group_chars:
            group_chars[root].sort(reverse=True)
        return "".join(group_chars[find(i)].pop() for i in range(length))
