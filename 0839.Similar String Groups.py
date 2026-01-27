class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        """Union-Find to count groups of similar anagram strings.

        Intuition:
            Two strings are similar if they differ in at most 2 positions.
            Use Union-Find to group similar strings transitively.

        Approach:
            1. For each pair of strings, check if they differ in <= 2 positions.
            2. If similar, union them in the disjoint set.
            3. Count the number of distinct roots.

        Complexity:
            Time: O(n^2 * m) where n = number of strings, m = string length
            Space: O(n)
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        num_strings, str_length = len(strs), len(strs[0])
        parent = list(range(num_strings))
        for i in range(num_strings):
            for j in range(i + 1, num_strings):
                if sum(strs[i][k] != strs[j][k] for k in range(str_length)) <= 2:
                    parent[find(i)] = find(j)
        return sum(i == find(i) for i in range(num_strings))
