class Node:
    def __init__(
        self, x: int, next: "Node | None" = None, random: "Node | None" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        """Two-Pass Hash Map Approach

        Intuition:
            First pass creates all copied nodes and maps originals to copies.
            Second pass assigns the random pointers using the mapping.

        Approach:
            Iterate through the original list, creating new nodes and building a
            dictionary from original to copy. Then iterate again to wire up the
            random pointers by looking up each original's random in the dictionary.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(n) for the hash map
        """
        node_map: dict[Node, Node] = {}
        dummy = tail = Node(0)
        current = head
        while current:
            tail.next = Node(current.val)
            tail = tail.next
            node_map[current] = tail
            current = current.next
        tail = dummy.next
        current = head
        while current:
            tail.random = node_map.get(current.random)
            tail = tail.next
            current = current.next
        return dummy.next
