from collections import deque


class Codec:
    """Serializes and deserializes a binary tree using level-order traversal.

    Intuition:
        BFS naturally captures the tree level by level. Using a sentinel
        value for null nodes preserves the complete structure so the tree
        can be reconstructed unambiguously.

    Approach:
        Serialize via BFS, outputting each node's value or '#' for null
        children, joined by commas. Deserialize by splitting the string,
        creating the root from the first token, then processing children
        in BFS order using a queue.

    Complexity:
        Time: O(n) for both serialize and deserialize
        Space: O(n) for the queue and output string
    """

    def serialize(self, root: "TreeNode | None") -> str:
        """Encode a tree to a single comma-separated string via BFS."""
        if root is None:
            return ""
        queue = deque([root])
        tokens: list[str] = []
        while queue:
            node = queue.popleft()
            if node:
                tokens.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                tokens.append("#")
        return ",".join(tokens)

    def deserialize(self, data: str) -> "TreeNode | None":
        """Decode a BFS-encoded string back into a binary tree."""
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root
