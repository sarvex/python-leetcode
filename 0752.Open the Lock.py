from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """BFS to find minimum turns from "0000" to target avoiding deadends.

        Intuition:
            Each state is a 4-digit combination. BFS from "0000" explores all
            reachable combinations level by level, guaranteeing the shortest path.

        Approach:
            1. Place all deadends in a visited set to avoid them.
            2. BFS from "0000", generating 8 neighbors per state (each digit
               can be incremented or decremented).
            3. Return the BFS depth when target is reached, or -1.

        Complexity:
            Time: O(10^4 * 4) — bounded by total states
            Space: O(10^4)
        """

        def generate_neighbors(state: str) -> list[str]:
            neighbors = []
            chars = list(state)
            for i in range(4):
                original = chars[i]
                chars[i] = "9" if original == "0" else str(int(original) - 1)
                neighbors.append("".join(chars))
                chars[i] = "0" if original == "9" else str(int(original) + 1)
                neighbors.append("".join(chars))
                chars[i] = original
            return neighbors

        if target == "0000":
            return 0
        visited = set(deadends)
        if "0000" in visited:
            return -1
        queue = deque(["0000"])
        visited.add("0000")
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                for neighbor in generate_neighbors(current):
                    if neighbor == target:
                        return steps
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        return -1
