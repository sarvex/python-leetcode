class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        """Find the lexicographically smallest string from leaf to root.

        Intuition:
            Build paths from root to each leaf, reverse them, and track the
            minimum string seen.

        Approach:
            DFS with backtracking, appending each node's character to the path.
            At every leaf, reverse the path and compare with the current best.

        Complexity:
            Time: O(n * h) where h is the height due to string comparison
            Space: O(h) for recursion stack and path
        """
        smallest = chr(ord("z") + 1)

        def dfs(node: TreeNode | None, path: list[str]) -> None:
            nonlocal smallest
            if node is None:
                return
            path.append(chr(ord("a") + node.val))
            if node.left is None and node.right is None:
                smallest = min(smallest, "".join(reversed(path)))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return smallest
