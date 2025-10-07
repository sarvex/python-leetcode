from collections import deque


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        """Track rainy and dry days to prevent lake flooding using greedy queue-based approach.

        Intuition:
        When a lake gets rain twice, we must have dried it between the two rains.
        Track dry days in a queue and use the first available dry day after the
        previous rain to dry the lake that's about to flood.

        Approach:
        - Maintain a hash map to track each lake's last rain index
        - Use a deque to store indices of dry days
        - On rainy day: check if lake already full, find next dry day after last rain
        - On dry day: add to queue (will assign which lake to dry later)
        - If no valid dry day exists between two rains, return empty array

        Complexity:
        Time: O(n * d) where n is length of rains, d is number of dry days (worst case O(n²))
        Space: O(n) for storing hash map, queue, and result
        """
        lake_last_rain = {}
        dry_days = deque([])
        result = []

        for index, lake in enumerate(rains):
            if lake:
                if lake in lake_last_rain:
                    for dry_index in dry_days:
                        if dry_index > lake_last_rain[lake]:
                            result[dry_index] = lake
                            dry_days.remove(dry_index)
                            break
                    else:
                        return []
                result.append(-1)
                lake_last_rain[lake] = index
            else:
                result.append(1)
                dry_days.append(index)

        return result
