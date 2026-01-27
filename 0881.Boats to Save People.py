class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """Two-pointer greedy pairing lightest with heaviest person.

        Intuition:
            Sort people by weight. Pair the lightest with the heaviest if
            they fit together; otherwise the heaviest goes alone.

        Approach:
            1. Sort the people array.
            2. Use two pointers at both ends.
            3. If the lightest and heaviest fit in one boat, advance both
               pointers. Otherwise, only the heaviest boards alone.
            4. Count each boat used.

        Complexity:
            Time: O(n log n)
            Space: O(1) excluding sort space
        """
        people.sort()
        boat_count = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boat_count += 1
        return boat_count
