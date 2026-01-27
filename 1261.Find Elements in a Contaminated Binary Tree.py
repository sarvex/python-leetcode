# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:
    """Recover a contaminated binary tree and support value lookups.

    Intuition:
        The tree follows the rule: root is 0, left child is 2*val+1, right
        child is 2*val+2. We can recover all values via DFS and store them
        in a set for O(1) lookup.

    Approach:
        In the constructor, set root value to 0 and DFS through the tree,
        assigning correct values and storing them in a set. The find method
        simply checks set membership.

    Complexity:
        Time: O(n) for construction, O(1) for find
        Space: O(n)
    """

    def __init__(self, root: "TreeNode | None") -> None:
        def dfs(node: "TreeNode | None") -> None:
            self.values.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)

        root.val = 0
        self.values: set[int] = set()
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.values
