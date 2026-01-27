# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
        """Delete given nodes and return the forest of remaining trees.

        Intuition:
            When a node is deleted, its children become new roots. Post-order
            traversal ensures children are processed before their parent.

        Approach:
            Use DFS post-order traversal. For each node, if it is in the
            delete set, add its non-null children to the result and return
            None to detach it from the parent.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(n) for the delete set and recursion stack
        """
        delete_set = set(to_delete)
        result: list[TreeNode] = []

        def dfs(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val not in delete_set:
                return node
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)
            return None

        if dfs(root):
            result.append(root)
        return result
