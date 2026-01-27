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
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        """Recover a Tree From Preorder Traversal using stack-based reconstruction.

        Intuition:
            The number of dashes before a value indicates the depth of that
            node. Use a stack to track the path from root to the current node,
            popping until the stack depth matches the target depth.

        Approach:
            Parse the string to extract depth (dash count) and node value pairs.
            Maintain a stack representing the current path. Pop nodes until the
            stack size equals the depth, then attach the new node as left or
            right child of the stack top.

        Complexity:
            Time: O(n) where n is the length of the traversal string
            Space: O(h) where h is the height of the tree
        """
        stack: list[TreeNode] = []
        index = 0
        length = len(traversal)

        while index < length:
            depth = 0
            while index < length and traversal[index] == "-":
                depth += 1
                index += 1

            value_str = ""
            while index < length and traversal[index] != "-":
                value_str += traversal[index]
                index += 1

            current = TreeNode(val=int(value_str))

            while len(stack) > depth:
                stack.pop()

            if stack:
                if stack[-1].left is None:
                    stack[-1].left = current
                else:
                    stack[-1].right = current

            stack.append(current)
        return stack[0]
