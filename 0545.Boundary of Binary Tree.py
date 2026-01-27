class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode | None) -> list[int]:
        """DFS to collect left boundary, leaves, and right boundary.

        Intuition:
            The boundary consists of the root, left boundary (excluding leaves),
            all leaves (left to right), and right boundary in reverse (excluding
            leaves).

        Approach:
            Use DFS with a mode parameter: 0 for left boundary, 1 for leaves,
            2 for right boundary. Collect each part separately and concatenate.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(values: list[int], node: TreeNode | None, mode: int) -> None:
            if node is None:
                return
            if mode == 0:
                if node.left != node.right:
                    values.append(node.val)
                    if node.left:
                        dfs(values, node.left, mode)
                    else:
                        dfs(values, node.right, mode)
            elif mode == 1:
                if node.left == node.right:
                    values.append(node.val)
                else:
                    dfs(values, node.left, mode)
                    dfs(values, node.right, mode)
            else:
                if node.left != node.right:
                    values.append(node.val)
                    if node.right:
                        dfs(values, node.right, mode)
                    else:
                        dfs(values, node.left, mode)

        result = [root.val]
        if root.left == root.right:
            return result
        left_boundary, leaves, right_boundary = [], [], []
        dfs(left_boundary, root.left, 0)
        dfs(leaves, root, 1)
        dfs(right_boundary, root.right, 2)
        result += left_boundary + leaves + right_boundary[::-1]
        return result
