class Solution:
    def validateBinaryTreeNodes(
        self, n: int, left_child: list[int], right_child: list[int]
    ) -> bool:
        """Validate whether n nodes form exactly one valid binary tree.

        Intuition:
            A valid binary tree requires that every non-root node has exactly
            one parent, and all nodes are connected. Union-Find detects cycles
            and multiple parents efficiently.

        Approach:
            Use Union-Find. For each node, attempt to union it with its
            children. If a child already has a parent (visited) or unioning
            creates a cycle (same root), return False. Track the number of
            connected components; it must be exactly 1 at the end.

        Complexity:
            Time: O(n * alpha(n)) which is nearly O(n).
            Space: O(n)
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(n))
        has_parent = [False] * n
        components = n

        for i, (left, right) in enumerate(zip(left_child, right_child)):
            for child in (left, right):
                if child != -1:
                    if has_parent[child] or find(i) == find(child):
                        return False
                    parent[find(i)] = find(child)
                    has_parent[child] = True
                    components -= 1

        return components == 1
