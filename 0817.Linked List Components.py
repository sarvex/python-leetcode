class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        """Count connected components in linked list by tracking group boundaries.

        Intuition:
            Walk the list and count how many contiguous groups of values
            exist that belong to the given set.

        Approach:
            1. Convert nums to a set for O(1) lookup.
            2. Traverse the linked list, skipping nodes not in the set.
            3. Each time we enter a group of nodes in the set, increment count.

        Complexity:
            Time: O(n)
            Space: O(m) where m = len(nums)
        """
        component_count = 0
        values_set = set(nums)
        while head:
            while head and head.val not in values_set:
                head = head.next
            component_count += head is not None
            while head and head.val in values_set:
                head = head.next
        return component_count
