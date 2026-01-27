class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        """Find path from root to label in zigzag-ordered binary tree.

        Intuition:
            In a zigzag tree, each level alternates direction. To find the
            parent, we first determine the level, then mirror the label within
            that level to account for the zigzag ordering.

        Approach:
            Determine the level of the label by finding the highest power of 2
            that fits. Build the path bottom-up by computing the mirrored parent
            at each level using the formula that maps a label to its complement
            within the level range.

        Complexity:
            Time: O(log n) where n is the label value
            Space: O(log n) for the result path
        """
        level_start = 1
        level = 1
        while (level_start << 1) <= label:
            level_start <<= 1
            level += 1
        path = [0] * level
        while level:
            path[level - 1] = label
            label = ((1 << (level - 1)) + (1 << level) - 1 - label) >> 1
            level -= 1
        return path
