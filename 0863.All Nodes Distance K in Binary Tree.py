class TreeNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        """DFS with parent pointers to find all nodes at distance k from target.

        Intuition:
        In a tree, distance-k nodes can be in the subtree of the target or
        reached by going up through ancestors. Building parent pointers
        allows bidirectional traversal from the target.

        Approach:
        1. DFS to build a parent map for every node
        2. From the target, DFS in all three directions (left, right, parent)
        3. Track visited nodes to avoid revisiting
        4. Collect nodes at exactly distance k

        Complexity:
        Time: O(n) where n is the number of nodes
        Space: O(n) for parent map and visited set
        """

        def build_parents(node: TreeNode | None, parent: TreeNode | None) -> None:
            if node is None:
                return
            parent_map[node] = parent
            build_parents(node.left, node)
            build_parents(node.right, node)

        def dfs(node: TreeNode | None, distance: int) -> None:
            if node is None or node.val in visited:
                return
            visited.add(node.val)
            if distance == 0:
                result.append(node.val)
                return
            dfs(node.left, distance - 1)
            dfs(node.right, distance - 1)
            dfs(parent_map[node], distance - 1)

        parent_map: dict[TreeNode, TreeNode | None] = {}
        build_parents(root, None)
        result: list[int] = []
        visited: set[int] = set()
        dfs(target, k)
        return result
