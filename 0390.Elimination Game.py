class Solution:
    def lastRemaining(self, n: int) -> int:
        """Simulate elimination game by tracking endpoints.

        Intuition:
            Instead of simulating the full list, track only the first
            and last elements. On each pass, the head or tail shifts
            based on direction and whether the count is odd.

        Approach:
            1. Track head (a1), tail (an), step size, count, and direction.
            2. On right-to-left pass (odd round), decrement tail; if count
               is odd, also shift head.
            3. On left-to-right pass (even round), increment head; if count
               is odd, also shift tail.
            4. Double the step, halve the count, flip direction each round.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        head, tail = 1, n
        round_index, step, count = 0, 1, n
        while count > 1:
            if round_index % 2:
                tail -= step
                if count % 2:
                    head += step
            else:
                head += step
                if count % 2:
                    tail -= step
            count >>= 1
            step <<= 1
            round_index += 1
        return head
