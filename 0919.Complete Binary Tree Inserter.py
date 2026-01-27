from collections import deque


class CBTInserter:
    """Level-order array representation for complete binary tree insertion.

    Intuition:
        A complete binary tree can be stored as an array where the parent of
        node at index i is at index (i-1)//2. This makes finding the next
        insertion point trivial.

    Approach:
        1. Initialize by performing BFS to store all nodes in array order.
        2. For insertion, find the parent using index arithmetic,
           create the new node, and attach it as left or right child.
        3. Return the root as the first element of the array.

    Complexity:
        Time: O(n) for init, O(1) for insert
        Space: O(n)
    """

    def __init__(self, root: TreeNode | None):
        self.tree: list[TreeNode] = []
        queue: deque[TreeNode] = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                self.tree.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.tree[(len(self.tree) - 1) // 2]
        node = TreeNode(val)
        self.tree.append(node)
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
        return parent.val

    def get_root(self) -> TreeNode | None:
        return self.tree[0]
