from collections import defaultdict, deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """BFS simulation of domino forces with timestamped propagation.

        Intuition:
            Each initially pushed domino creates a force wave. Using BFS with
            timestamps, we can determine which dominoes get pushed and handle
            simultaneous opposing forces (which cancel out).

        Approach:
            1. Initialize a queue with all non-dot positions and their forces.
            2. BFS: propagate each force to the next domino in its direction.
            3. If a domino receives two forces at the same time, they cancel.
            4. If only one force arrives, apply it and continue propagation.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(dominoes)
        queue: deque[int] = deque()
        timestamp = [-1] * length
        forces: defaultdict[int, list[str]] = defaultdict(list)
        for i, direction in enumerate(dominoes):
            if direction != ".":
                queue.append(i)
                timestamp[i] = 0
                forces[i].append(direction)
        result = ["."] * length
        while queue:
            position = queue.popleft()
            if len(forces[position]) == 1:
                result[position] = direction = forces[position][0]
                next_pos = position - 1 if direction == "L" else position + 1
                if 0 <= next_pos < length:
                    current_time = timestamp[position]
                    if timestamp[next_pos] == -1:
                        queue.append(next_pos)
                        timestamp[next_pos] = current_time + 1
                        forces[next_pos].append(direction)
                    elif timestamp[next_pos] == current_time + 1:
                        forces[next_pos].append(direction)
        return "".join(result)
