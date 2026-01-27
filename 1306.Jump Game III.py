from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        """Determine if index with value 0 is reachable by jumping arr[i] steps.

        Intuition:
            BFS from the start index, jumping forward and backward by arr[i] steps,
            until a zero-value index is found.

        Approach:
            Use BFS with a queue. Mark visited indices by setting their value to -1
            to avoid revisiting. Return True when a zero-value cell is reached.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        queue = deque([start])
        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            jump = arr[index]
            arr[index] = -1
            for neighbor in (index + jump, index - jump):
                if 0 <= neighbor < len(arr) and arr[neighbor] >= 0:
                    queue.append(neighbor)
        return False
