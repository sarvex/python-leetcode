class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        """Recursive Tree Construction

        Intuition:
            For each value in [1, n], use it as the root. All smaller values
            form the left subtree and all larger values form the right subtree.
            Combine every possible left and right subtree pair.

        Approach:
            Use a recursive function parameterized by the range [start, end].
            For each root value in the range, recursively generate all left
            and right subtrees, then combine them with the root. Base case:
            when start > end, return [None].

        Complexity:
            Time: O(n * C(n)) where C(n) is the n-th Catalan number
            Space: O(n * C(n))
        """

        def dfs(start: int, end: int) -> list[TreeNode | None]:
            if start > end:
                return [None]
            trees: list[TreeNode | None] = []
            for root_val in range(start, end + 1):
                left_trees = dfs(start, root_val - 1)
                right_trees = dfs(root_val + 1, end)
                for left_subtree in left_trees:
                    for right_subtree in right_trees:
                        trees.append(TreeNode(root_val, left_subtree, right_subtree))
            return trees

        return dfs(1, n)
