class Solution:
    def treeToDoublyList(self, root: "Node | None") -> "Node | None":
        """In-order traversal linking nodes into a sorted circular doubly linked list.

        Intuition:
            An in-order traversal of a BST visits nodes in sorted order. By
            linking each visited node to the previously visited one, we form
            a doubly linked list.

        Approach:
            1. Perform in-order DFS, maintaining a previous pointer.
            2. Link previous.right to current and current.left to previous.
            3. Track the head (first node visited).
            4. After traversal, connect head and tail to form a circular list.

        Complexity:
            Time: O(n) where n is the number of nodes.
            Space: O(h) for recursion stack where h is the tree height.
        """

        def dfs(node: "Node | None") -> None:
            if node is None:
                return
            nonlocal prev, head
            dfs(node.left)
            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node
            prev = node
            dfs(node.right)

        if root is None:
            return None
        head = prev = None
        dfs(root)
        prev.right = head
        head.left = prev
        return head
