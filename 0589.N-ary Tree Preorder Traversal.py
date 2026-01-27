class Solution:
    def preorder(self, root: "Node") -> list[int]:
        """N-ary tree preorder traversal using recursive DFS.

        Intuition:
            Visit the current node first, then recursively visit all children
            from left to right, collecting values in preorder sequence.

        Approach:
            1. Use a recursive DFS helper function.
            2. Append the current node's value before visiting children.
            3. Iterate through all children and recurse on each.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(node: "Node") -> None:
            if node is None:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)

        result: list[int] = []
        dfs(root)
        return result
