class Solution:
    def insert(self, head: "Node | None", insertVal: int) -> "Node":
        """Insert into a sorted circular linked list maintaining order.

        Intuition:
            Find the correct position by traversing the circular list. The
            insertion point is either between two nodes in sorted order, at
            the wrap-around point (max to min), or after a full cycle if all
            values are equal.

        Approach:
            1. Handle empty list: create a self-referencing node.
            2. Traverse from head, looking for the insertion point where
               prev.val <= insertVal <= curr.val (normal case) or at the
               wrap-around boundary where prev.val > curr.val and insertVal
               is >= prev or <= curr.
            3. If no position found after a full cycle, insert after head.

        Complexity:
            Time: O(n) single traversal of the circular list
            Space: O(1) constant extra space
        """
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        previous, current = head, head.next
        while current != head:
            if previous.val <= insertVal <= current.val or (
                previous.val > current.val
                and (insertVal >= previous.val or insertVal <= current.val)
            ):
                break
            previous, current = current, current.next
        previous.next = node
        node.next = current
        return head
