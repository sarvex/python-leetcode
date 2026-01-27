class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        """DFS traversal collecting root-to-leaf paths as strings.

        Intuition:
            Traverse the tree depth-first, building the path string as we go.
            When a leaf node is reached, join the accumulated values with "->".

        Approach:
            1. Use a recursive DFS helper that appends the current node value to a path list.
            2. If the current node is a leaf, join the path list and add to results.
            3. Otherwise, recurse into left and right children.
            4. Backtrack by popping the last element after processing.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(n) for the recursion stack and path storage
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                result.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        result: list[str] = []
        path: list[str] = []
        dfs(root)
        return result
