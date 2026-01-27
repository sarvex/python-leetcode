from math import inf


class Solution:
    def closestValue(self, root: TreeNode | None, target: float) -> int:
        """BST traversal following the target direction to find the closest value.

        Intuition:
            Exploit BST properties to navigate toward the target, updating the
            closest value whenever a nearer node is found.

        Approach:
            1. Use recursive DFS starting from the root.
            2. At each node, compute the distance to target and update the answer
               if this node is closer (or equal distance but smaller value).
            3. Navigate left or right based on whether target is smaller or larger
               than the current node value.

        Complexity:
            Time: O(h) where h is the height of the tree
            Space: O(h) for the recursion stack
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            distance = abs(target - node.val)
            nonlocal closest_val, min_diff
            if distance < min_diff or (distance == min_diff and node.val < closest_val):
                min_diff = distance
                closest_val = node.val
            node = node.left if target < node.val else node.right
            dfs(node)

        closest_val = 0
        min_diff = inf
        dfs(root)
        return closest_val
