from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two sorted linked lists using an iterative approach.

        Intuition:
            Use a dummy head to simplify edge cases and iterate through both lists,
            always choosing the smaller value to add to our result list.

        Approach:
            1. Create a dummy head and a current pointer
            2. Iterate through both lists simultaneously
            3. Compare values and link the smaller node to our result list
            4. Advance the pointer in the list from which we took the node
            5. After one list is exhausted, link the remainder of the other list

        Complexity:
            Time: O(n + m) where n and m are the lengths of the two lists
            Space: O(1) as we only use constant extra space
        """
        # Create dummy head to simplify edge cases
        dummy = ListNode(-1)
        current = dummy

        # Handle empty list cases
        if not list1:
            return list2
        if not list2:
            return list1

        # Iterate through both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Link the remainder of whichever list is not exhausted
        current.next = list1 if list1 else list2

        return dummy.next

        """Merge two sorted linked lists using a recursive approach.

        Intuition:
            Use recursion to merge lists by selecting the smaller head node
            and recursively merging the rest.

        Approach:
            1. Handle base cases (empty lists)
            2. Compare the values of the head nodes
            3. Recursively merge the rest of the lists

        Complexity:
            Time: O(n + m) where n and m are the lengths of the two lists
            Space: O(n + m) due to the recursion stack
        """
        # Base case: if either list is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1

        # Recursive case: choose the smaller head and merge the rest
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2
