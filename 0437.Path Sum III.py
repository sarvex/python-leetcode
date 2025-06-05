from typing import Optional
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """Prefix Sum with Hashmap approach for finding paths with target sum.

        Intuition:
        Use a prefix sum approach with a hashmap to track running sums. When the difference
        between current sum and target exists in our hashmap, we've found valid paths.

        Approach:
        1. Use a counter to track frequency of prefix sums encountered so far
        2. Initialize counter with {0: 1} to handle paths starting from root
        3. Perform DFS, updating the running sum at each node
        4. For each node, check if (current_sum - targetSum) exists in our counter
        5. Increment counter for current sum before exploring children
        6. Decrement counter after exploring to maintain correct state for parallel paths

        Complexity:
        Time: O(n) where n is the number of nodes in the tree
        Space: O(h) where h is the height of the tree (recursion stack) + O(n) for counter
        """
        prefix_sums = Counter({0: 1})

        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if node is None:
                return 0

            # Update current sum with this node's value
            current_sum += node.val

            # Check if we have any valid paths ending at current node
            # (current_sum - targetSum) represents the prefix sum we need to have seen before
            path_count = prefix_sums[current_sum - targetSum]

            # Add current sum to our prefix sums counter
            prefix_sums[current_sum] += 1

            # Explore left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)

            # Backtrack: remove current sum from counter when going up
            # This ensures prefix sums are only counted in current path
            prefix_sums[current_sum] -= 1

            return path_count

        return dfs(root, 0)
