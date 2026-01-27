class Codec:
    """Encodes N-ary trees to binary trees and decodes back.

    Uses left-child right-sibling representation: the first child becomes the
    left child of the binary node, and subsequent siblings chain as right children.
    """

    def encode(self, root: "Node | None") -> "TreeNode | None":
        """Encode an N-ary tree to a binary tree using left-child right-sibling.

        Intuition:
            Map the first child to left and siblings to right in binary tree form.

        Approach:
            1. If root is None, return None.
            2. Create a binary TreeNode with root's value.
            3. Recursively encode the first child as left subtree.
            4. Chain remaining children as right subtrees of the left node.

        Complexity:
            Time: O(n) where n is the number of nodes.
            Space: O(h) for recursion depth.
        """
        if root is None:
            return None
        binary_node = TreeNode(root.val)
        if not root.children:
            return binary_node
        left = self.encode(root.children[0])
        binary_node.left = left
        for child in root.children[1:]:
            left.right = self.encode(child)
            left = left.right
        return binary_node

    def decode(self, data: "TreeNode | None") -> "Node | None":
        """Decode a binary tree back to an N-ary tree.

        Intuition:
            Reverse the left-child right-sibling encoding by collecting all
            right children as siblings of the first child.

        Approach:
            1. If data is None, return None.
            2. Create an N-ary Node with data's value and empty children list.
            3. Traverse the left child's right chain, decoding each as a child.

        Complexity:
            Time: O(n) where n is the number of nodes.
            Space: O(h) for recursion depth.
        """
        if data is None:
            return None
        nary_node = Node(data.val, [])
        if data.left is None:
            return nary_node
        left = data.left
        while left:
            nary_node.children.append(self.decode(left))
            left = left.right
        return nary_node
