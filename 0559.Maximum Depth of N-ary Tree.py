class Solution:
    def maxDepth(self, root: "Node") -> int:
        """Find maximum depth of N-ary tree using recursion.

        Intuition:
            The depth of a tree is 1 plus the maximum depth among all its
            children. An empty tree has depth 0.

        Approach:
            1. Base case: if root is None, return 0.
            2. Recursively compute the max depth of all children.
            3. Return 1 + max child depth.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the height of the tree
        """
        if root is None:
            return 0
        return 1 + max([self.maxDepth(child) for child in root.children], default=0)
