class Solution:
    def flatten(self, head: "Node") -> "Node":
        """Recursive preorder traversal to flatten a multilevel doubly linked list.

        Intuition:
            Process each node by linking it after the previous node. If a child
            exists, recurse into the child list before continuing with next.

        Approach:
            1. Use a dummy node as the starting previous node.
            2. Recursively process: link current to previous, then recurse into
               child (saving next), clear child pointer, then recurse into saved next.
            3. Return the tail of the processed segment.
            4. Disconnect the dummy from the result and return dummy.next.

        Complexity:
            Time: O(n) where n is the total number of nodes.
            Space: O(n) for recursion stack in the worst case.
        """

        def preorder(previous: "Node", current: "Node | None") -> "Node":
            if current is None:
                return previous
            current.prev = previous
            previous.next = current

            next_node = current.next
            tail = preorder(current, current.child)
            current.child = None
            return preorder(tail, next_node)

        if head is None:
            return None
        dummy = Node(0, None, head, None)
        preorder(dummy, head)
        dummy.next.prev = None
        return dummy.next
