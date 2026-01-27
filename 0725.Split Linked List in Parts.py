class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        """Split linked list into k consecutive parts as evenly as possible.

        Intuition:
            Compute the total length, then divide into k parts where the first
            few parts get one extra node to distribute the remainder.

        Approach:
            1. Count the total number of nodes.
            2. Compute base part size and how many parts get an extra node.
            3. Iterate through the list, cutting it into k segments.

        Complexity:
            Time: O(n + k) where n is the number of nodes
            Space: O(k) for the result array
        """
        total_length = 0
        current = head
        while current:
            total_length += 1
            current = current.next
        part_size, extra = divmod(total_length, k)
        parts: list[ListNode | None] = [None] * k
        current = head
        for i in range(k):
            if current is None:
                break
            parts[i] = current
            segment_length = part_size + int(i < extra)
            for _ in range(1, segment_length):
                current = current.next
            next_head = current.next
            current.next = None
            current = next_head
        return parts
