# Definition for singly-linked list.
from heapq import heapify, heappop, heappush
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge k sorted linked lists into one sorted linked list.

        Intuition: Use a min-heap to efficiently find the smallest node among all lists.

        Approach:
        1. Define a comparison method for ListNode to use in the heap
        2. Initialize a min-heap with the first node of each list
        3. Repeatedly pop the smallest node, add its next node to the heap,
           and connect the nodes to form the result list

        Complexity:
        Time: O(N log k) where N is the total number of nodes and k is the number of lists
        Space: O(k) for the heap which stores at most k nodes
        """
        # Define comparison for ListNode to use in min-heap
        def __lt__(a: ListNode, b: ListNode) -> bool:
            return a.val < b.val

        # Temporarily add __lt__ method to ListNode class
        setattr(ListNode, "__lt__", __lt__)

        # Initialize min-heap with first node of each list (if not empty)
        pq = [head for head in lists if head]
        heapify(pq)

        # Create dummy head for result list
        dummy = ListNode()
        current = dummy

        # Build result list by repeatedly taking smallest node
        while pq:
            # Get smallest node
            node = heappop(pq)

            # Add next node to heap if it exists
            if node.next:
                heappush(pq, node.next)

            # Add current smallest node to result list
            current.next = node
            current = current.next

        return dummy.next
