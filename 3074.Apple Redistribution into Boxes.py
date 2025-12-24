from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Sort capacity in descending order to use largest boxes first
        capacity.sort(reverse=True)

        total_apples = sum(apple)
        current_capacity = 0

        for i, box_capacity in enumerate(capacity):
            current_capacity += box_capacity
            if current_capacity >= total_apples:
                return i + 1

        return len(capacity)
