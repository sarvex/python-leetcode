class Solution:
    def postorder(self, root: "Node") -> list[int]:
        """N-ary tree postorder traversal using recursive DFS.

        Intuition:
            Visit all children first from left to right, then visit the
            current node, collecting values in postorder sequence.

        Approach:
            1. Use a recursive DFS helper function.
            2. Recurse on all children before appending the current node's value.
            3. Collect results in a list and return.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(node: "Node") -> None:
            if node is None:
                return
            for child in node.children:
                dfs(child)
            result.append(node.val)

        result: list[int] = []
        dfs(root)
        return result
