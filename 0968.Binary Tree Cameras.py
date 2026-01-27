import math


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
    def minCameraCover(self, root: TreeNode | None) -> int:
        """Post-order DFS with three states to minimize cameras covering all nodes.

        Intuition:
        Each node has three states: (a) has a camera, (b) covered by a child's
        camera, (c) covered by a parent's camera. By computing minimum cameras
        bottom-up, we optimally place cameras at every other level.

        Approach:
        1. DFS returns three values per node: cost with camera, covered by child,
           covered by parent
        2. Null nodes return (inf, 0, 0) since they need no coverage
        3. Combine left and right subtree costs using min combinations
        4. Answer is min of having camera at root or being covered by child

        Complexity:
        Time: O(n) where n is the number of nodes
        Space: O(h) where h is the tree height for recursion stack
        """

        def search(node: TreeNode | None) -> tuple[float, float, float]:
            if node is None:
                return math.inf, 0, 0
            left_cam, left_child_cov, left_parent_cov = search(node.left)
            right_cam, right_child_cov, right_parent_cov = search(node.right)
            has_camera = (
                min(left_cam, left_child_cov, left_parent_cov)
                + min(right_cam, right_child_cov, right_parent_cov)
                + 1
            )
            covered_by_child = min(
                left_cam + right_child_cov,
                left_child_cov + right_cam,
                left_cam + right_cam,
            )
            covered_by_parent = left_child_cov + right_child_cov
            return has_camera, covered_by_child, covered_by_parent

        cam, child_cov, _ = search(root)
        return int(min(cam, child_cov))
