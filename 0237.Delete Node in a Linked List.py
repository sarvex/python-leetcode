class Solution:
    def deleteNode(self, node: "ListNode") -> None:
        """Copy-and-skip to delete a node without access to head.

        Intuition:
            Since we cannot access the previous node, we copy the next node's
            value into the current node and skip over the next node.

        Approach:
            Copy the value of the next node into the given node, then set
            the given node's next pointer to skip the next node entirely.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        node.val = node.next.val
        node.next = node.next.next
