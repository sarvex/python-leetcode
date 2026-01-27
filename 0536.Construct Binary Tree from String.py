class Solution:
    def str2tree(self, s: str) -> TreeNode | None:
        """Recursive parsing of parenthesized string to build binary tree.

        Intuition:
            The string format is "val(left)(right)". Parse the root value,
            then recursively build left and right subtrees from parenthesized
            substrings.

        Approach:
            Find the first '(' to separate the root value. Track parenthesis
            depth to find the boundary between left and right subtrees.
            Recursively build each subtree.

        Complexity:
            Time: O(n^2) worst case due to string slicing
            Space: O(n) for recursion stack
        """

        def parse(text: str) -> TreeNode | None:
            if not text:
                return None
            paren_pos = text.find("(")
            if paren_pos == -1:
                return TreeNode(int(text))
            root = TreeNode(int(text[:paren_pos]))
            start = paren_pos
            depth = 0
            for i in range(paren_pos, len(text)):
                if text[i] == "(":
                    depth += 1
                elif text[i] == ")":
                    depth -= 1
                if depth == 0:
                    if start == paren_pos:
                        root.left = parse(text[start + 1 : i])
                        start = i + 1
                    else:
                        root.right = parse(text[start + 1 : i])
            return root

        return parse(s)
