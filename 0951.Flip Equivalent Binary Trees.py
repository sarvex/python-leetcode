# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        """Recursive DFS checking both flipped and unflipped subtree arrangements.

        Intuition:
            Two trees are flip equivalent if they are identical or become identical
            after swapping left and right children at some nodes. Check both
            possibilities recursively.

        Approach:
            1. Base cases: both None -> True; one None or different values -> False.
            2. Recursively check if children match without flipping.
            3. Also check if children match with flipping (left-right swap).
            4. Return True if either arrangement works.

        Complexity:
            Time: O(n) — visit each node at most a constant number of times
            Space: O(h) — recursion stack depth equals tree height
        """

        def dfs(node1: TreeNode | None, node2: TreeNode | None) -> bool:
            if node1 == node2 or (node1 is None and node2 is None):
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            return (dfs(node1.left, node2.left) and dfs(node1.right, node2.right)) or (
                dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            )

        return dfs(root1, root2)
