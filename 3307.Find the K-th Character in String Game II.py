from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """Binary tree traversal to find the k-th character in the string game.

        Intuition:
        The problem can be modeled as a binary tree where each level doubles in size.
        We need to locate the k-th position and track operations applied along the path.

        Approach:
        1. Find the depth of the tree needed to reach position k
        2. Traverse down the tree, tracking which half of each level contains k
        3. Apply operations when moving to the right half
        4. Convert the final accumulated value to a character

        Complexity:
        Time: O(log k) - We perform binary search through the virtual tree
        Space: O(1) - We use constant extra space
        """
        # Find the smallest level where k fits
        tree_size, level = 1, 0
        while tree_size < k:
            tree_size *= 2
            level += 1

        # Traverse down the tree to find the character
        accumulated_ops = 0
        while tree_size > 1:
            half_size = tree_size // 2

            # If k is in the right half
            if k > half_size:
                k -= half_size  # Adjust k to be relative to right subtree
                accumulated_ops += operations[level - 1]  # Apply operation for this level

            tree_size = half_size
            level -= 1

        # Convert to lowercase letter (a-z)
        return chr(accumulated_ops % 26 + ord("a"))
