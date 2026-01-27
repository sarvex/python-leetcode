class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        """Convert linked list to array then recursively build balanced BST.

        Intuition:
            A sorted linked list can be converted to an array for O(1) index
            access, then the same mid-point partitioning strategy builds a
            height-balanced BST.

        Approach:
            1. Traverse the linked list to collect all values into an array.
            2. Recursively select the middle element as root.
            3. Build left and right subtrees from the respective halves.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def build_bst(values: list[int], start: int, end: int) -> TreeNode | None:
            if start > end:
                return None
            mid = (start + end) >> 1
            return TreeNode(
                values[mid],
                build_bst(values, start, mid - 1),
                build_bst(values, mid + 1, end),
            )

        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return build_bst(values, 0, len(values) - 1)
