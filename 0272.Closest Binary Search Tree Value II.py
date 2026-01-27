from collections import deque


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> list[int]:
        """In-order traversal with a sliding window deque to find k closest values.

        Intuition:
            In-order traversal of a BST yields sorted values. We can maintain a
            deque of size k and replace the front element when a closer value is
            found, since sorted order guarantees once a value is farther than the
            front, all subsequent values will also be farther.

        Approach:
            1. Perform in-order DFS traversal.
            2. Maintain a deque of at most k values.
            3. If the deque has k elements and the current value is not closer
               than the front, stop early.
            4. Otherwise, remove the front and append the current value.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(k + h) for the deque and recursion stack
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            dfs(node.left)
            if len(window) < k:
                window.append(node.val)
            else:
                if abs(node.val - target) >= abs(window[0] - target):
                    return
                window.popleft()
                window.append(node.val)
            dfs(node.right)

        window: deque[int] = deque()
        dfs(root)
        return list(window)
