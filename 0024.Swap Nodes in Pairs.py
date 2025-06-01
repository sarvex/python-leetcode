from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursively swap every two adjacent nodes in a linked list

        Intuition:
        Use recursion to swap pairs of nodes, working from the head of the list.
        Each recursive call handles one pair of nodes and returns the new head.

        Approach:
        1. Base case: If the list has 0 or 1 nodes, return the head as is
        2. For each pair:
           - Recursively process the rest of the list (starting from the 3rd node)
           - Swap the current pair by adjusting the next pointers
           - Return the new head (which was originally the second node)

        Complexity:
        Time: O(n) where n is the number of nodes in the list
        Space: O(n) due to the recursion stack
        """
        # Base case: empty list or only one node
        if head is None or head.next is None:
            return head

        # Store the second node as the new head after swapping
        new_head = head.next

        # Recursively swap the remaining pairs
        head.next = self.swapPairs(new_head.next)

        # Connect the second node to the first node
        new_head.next = head

        # Return the new head of this sublist
        return new_head

    def swapPairs_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iteratively swap every two adjacent nodes in a linked list

        Intuition:
        Use a dummy node and iterate through the list, swapping pairs as we go.

        Approach:
        1. Create a dummy node pointing to the head
        2. Use a prev pointer to track the node before each pair
        3. For each pair:
           - Adjust the pointers to swap the pair
           - Move prev to the next pair
        4. Return the new head (dummy.next)

        Complexity:
        Time: O(n) where n is the number of nodes in the list
        Space: O(1) as we only use a constant amount of extra space
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Iterate through the list
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = first.next

            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next
