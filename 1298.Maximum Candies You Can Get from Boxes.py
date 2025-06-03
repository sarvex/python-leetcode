from typing import List, Set


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                  containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """Iterative approach processing boxes in batches until convergence

        Intuition:
        Instead of tracking processed boxes, we can repeatedly process all available boxes
        in batches until we can't collect any more candies. This approach is simpler and
        eliminates the need for complex tracking data structures.

        Approach:
        1. Start with the initial boxes as our processing queue
        2. Keep track of all keys we've collected
        3. In each iteration:
           - Process boxes we can open (either by status or collected keys)
           - Collect candies, keys, and new boxes
           - Continue until no more candies can be collected

        Complexity:
        Time: O(N²) where N is the total number of boxes (worst case if each iteration only opens one box)
        Space: O(N) for storing keys and the processing queue
        """
        # Initialize processing queue with initial boxes
        processing_queue = initialBoxes

        # Track collected keys
        collected_keys: Set[int] = set()

        # Track total candies collected
        total_candies = 0

        # Previous iteration candy count to detect convergence
        previous_candy_count = None

        # Continue until no more candies can be collected
        while total_candies != previous_candy_count:
            previous_candy_count = total_candies
            next_queue = []

            # Process current batch of boxes
            for box in processing_queue:
                # Check if we can open this box (either by status or collected keys)
                if box in collected_keys or status[box]:
                    # Collect candies from this box
                    total_candies += candies[box]

                    # Collect keys from this box
                    collected_keys.update(keys[box])

                    # Add new boxes to the next processing batch
                    next_queue.extend(containedBoxes[box])
                else:
                    # Can't open this box yet, keep it for the next iteration
                    next_queue.append(box)

            # Update processing queue for next iteration
            processing_queue = next_queue

        return total_candies
