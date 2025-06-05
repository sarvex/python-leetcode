class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """Union-find with lexicographically smallest representative

        Intuition:
        Characters can be equivalent to each other, forming equivalence classes.
        For each class, we want to map all characters to the lexicographically smallest one.

        Approach:
        1. Use Union-Find data structure to group equivalent characters
        2. When merging two groups, always make the lexicographically smaller character the representative
        3. For each character in baseStr, find its representative and use it in the result

        Complexity:
        Time: O(n + m), where n is length of s1/s2 and m is length of baseStr
        Space: O(1), as we use a fixed-size array of 26 characters
        """
        # Initialize parent array where each character is its own parent
        parents = list(range(26))

        def find(x: int) -> int:
            """Find the representative of character x with path compression"""
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x: int, y: int) -> None:
            """Union two characters, making the lexicographically smaller one the representative"""
            root_x, root_y = find(x), find(y)
            if root_x < root_y:
                parents[root_y] = root_x
            else:
                parents[root_x] = root_y

        # Build the equivalence classes
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        # Map each character in baseStr to its lexicographically smallest equivalent
        result = []
        for char in baseStr:
            char_idx = ord(char) - ord('a')
            result.append(chr(find(char_idx) + ord('a')))

        return ''.join(result)
