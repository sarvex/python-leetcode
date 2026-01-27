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
    def flipMatchVoyage(self, root: TreeNode | None, voyage: list[int]) -> list[int]:
        """DFS preorder traversal with selective child swaps to match the voyage.

        Intuition:
        Traverse the tree in preorder and compare with the voyage sequence.
        When the left child doesn't match the next expected value, flip the
        children and continue with right-first traversal.

        Approach:
        1. DFS in preorder, comparing each node value with voyage[i]
        2. If mismatch, mark as impossible
        3. If left child exists but doesn't match next voyage value, record flip
           and traverse right before left
        4. Return flips or [-1] if impossible

        Complexity:
        Time: O(n) where n is the number of nodes
        Space: O(n) for recursion stack and result list
        """
        flips: list[int] = []
        index = 0
        is_valid = True

        def dfs(node: TreeNode | None) -> None:
            nonlocal index, is_valid
            if node is None or not is_valid:
                return
            if node.val != voyage[index]:
                is_valid = False
                return
            index += 1
            if node.left is None or node.left.val == voyage[index]:
                dfs(node.left)
                dfs(node.right)
            else:
                flips.append(node.val)
                dfs(node.right)
                dfs(node.left)

        dfs(root)
        return flips if is_valid else [-1]
