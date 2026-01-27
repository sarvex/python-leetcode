class Solution:
    def findTarget(self, root: "TreeNode | None", k: int) -> bool:
        """DFS with hash set to find two nodes summing to target in BST.

        Intuition:
        Traverse the tree and for each node check if its complement (k - val)
        has been seen before, similar to the classic two-sum approach.

        Approach:
        1. Use DFS to traverse the tree.
        2. For each node, check if k - node.val exists in a visited set.
        3. If found, return True; otherwise add node.val to the set.
        4. Recurse on both subtrees.

        Complexity:
        Time: O(n)
        Space: O(n)
        """

        def dfs(node: "TreeNode | None") -> bool:
            if node is None:
                return False
            if k - node.val in visited:
                return True
            visited.add(node.val)
            return dfs(node.left) or dfs(node.right)

        visited: set[int] = set()
        return dfs(root)
