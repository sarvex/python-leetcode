from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """Bitwise left shift approach to convert binary linked list to decimal.

        Intuition:
        Each binary digit position represents a power of 2. As we traverse the linked list,
        we can shift our result left by 1 (multiply by 2) and add the current node's value.
        This is equivalent to how we would convert a binary string to decimal.

        Approach:
        1. Initialize result to 0
        2. For each node in the linked list:
           a. Shift result left by 1 bit (multiply by 2)
           b. OR the result with current node's value (add current bit)
           c. Move to next node
        3. Return the final result

        Complexity:
        Time: O(n) where n is the number of nodes in the linked list
        Space: O(1) as we only use a single variable for the result
        """
        result = 0
        current = head

        while current:
            # Left shift by 1 and OR with current bit
            result = (result << 1) | current.val
            current = current.next

        return result
