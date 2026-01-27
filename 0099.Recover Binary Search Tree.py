class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """Inorder Traversal to Find Swapped Nodes

        Intuition:
            In a valid BST, inorder traversal yields sorted values. When two
            nodes are swapped, there will be one or two places where a node
            is greater than its successor in the inorder sequence.

        Approach:
            Perform inorder DFS while tracking the previous node. When
            prev.val > current.val, record the first offending node as
            'first' (the prev) and keep updating 'second' (the current).
            After traversal, swap the values of first and second to restore
            the BST.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            nonlocal prev, first, second
            dfs(node.left)
            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            prev = node
            dfs(node.right)

        prev = first = second = None
        dfs(root)
        first.val, second.val = second.val, first.val
