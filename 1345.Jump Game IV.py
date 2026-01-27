from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        """Find minimum jumps to reach the last index from index 0.

        Intuition:
            BFS gives shortest path. From each index, you can jump to i-1, i+1,
            or any index with the same value. Clear value groups after processing
            to avoid revisiting.

        Approach:
            Build a value-to-indices map. BFS from index 0, exploring neighbors
            (i-1, i+1) and same-value indices. Delete processed value groups
            to prevent redundant traversal.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        value_indices: dict[int, list[int]] = defaultdict(list)
        for i, val in enumerate(arr):
            value_indices[val].append(i)
        queue: deque[tuple[int, int]] = deque([(0, 0)])
        visited: set[int] = {0}
        while queue:
            index, steps = queue.popleft()
            if index == len(arr) - 1:
                return steps
            current_val = arr[index]
            next_step = steps + 1
            for neighbor in value_indices[current_val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, next_step))
            del value_indices[current_val]
            if index + 1 < len(arr) and (index + 1) not in visited:
                visited.add(index + 1)
                queue.append((index + 1, next_step))
            if index - 1 >= 0 and (index - 1) not in visited:
                visited.add(index - 1)
                queue.append((index - 1, next_step))
        return -1
