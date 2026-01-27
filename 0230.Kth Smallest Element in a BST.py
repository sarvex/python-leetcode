class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """Iterative inorder traversal to find the kth smallest element.

        Intuition:
            Inorder traversal of a BST yields elements in sorted order.
            Stop at the kth element.

        Approach:
            1. Use an explicit stack for iterative inorder traversal.
            2. Push left children until reaching a leaf.
            3. Pop a node, decrement k, and return its value when k reaches 0.
            4. Move to the right subtree and repeat.

        Complexity:
            Time: O(H + k) where H is the tree height
            Space: O(H) for the stack
        """
        stack: list[TreeNode] = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                k -= 1
                if k == 0:
                    return current.val
                current = current.right
