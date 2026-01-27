class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        """Inorder traversal to find mode(s) in BST without extra space.

        Intuition:
            An inorder traversal of a BST yields sorted values. We can track
            the current streak and compare with the maximum frequency to find modes.

        Approach:
            Perform inorder DFS, tracking the previous value, current count,
            and maximum count. When count exceeds max, reset the result list.
            When equal, append to the result list.

        Complexity:
            Time: O(n)
            Space: O(h) where h is tree height for recursion stack
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            nonlocal max_count, previous, result, current_count
            dfs(node.left)
            current_count = current_count + 1 if previous == node.val else 1
            if current_count > max_count:
                result = [node.val]
                max_count = current_count
            elif current_count == max_count:
                result.append(node.val)
            previous = node.val
            dfs(node.right)

        previous = None
        max_count = current_count = 0
        result: list[int] = []
        dfs(root)
        return result
