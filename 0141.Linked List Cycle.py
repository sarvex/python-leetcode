class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: ListNode | None = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """Hash Set Visited Nodes Approach

        Intuition:
            If a cycle exists, we will visit the same node twice during traversal.
            A set can track visited nodes for O(1) lookup.

        Approach:
            Traverse the linked list, adding each node to a set. If a node is
            already in the set, a cycle exists. If we reach the end (None),
            there is no cycle.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(n) for the visited set
        """
        visited: set[ListNode] = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
