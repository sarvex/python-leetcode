from collections import deque


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        """Reverse topological BFS to find stamping order.

        Intuition:
            Work backwards — find positions where the stamp matches the target,
            then mark those characters as wildcards that match anything, revealing
            new valid stamp positions.

        Approach:
            1. Build in-degree for each window position based on mismatches.
            2. Start BFS from windows with zero mismatches (perfect match).
            3. When stamping a window, mark its characters as visited (wildcards).
            4. Visited characters reduce in-degrees of overlapping windows.
            5. Reverse the order of stamps found for the final answer.

        Complexity:
            Time: O(n * m) — where n is target length, m is stamp length
            Space: O(n * m) — for adjacency lists and visited tracking
        """
        stamp_len, target_len = len(stamp), len(target)
        in_degree = [stamp_len] * (target_len - stamp_len + 1)
        queue = deque()
        adjacency = [[] for _ in range(target_len)]
        for window_start in range(target_len - stamp_len + 1):
            for offset, stamp_char in enumerate(stamp):
                if target[window_start + offset] == stamp_char:
                    in_degree[window_start] -= 1
                    if in_degree[window_start] == 0:
                        queue.append(window_start)
                else:
                    adjacency[window_start + offset].append(window_start)
        result = []
        visited = [False] * target_len
        while queue:
            window_start = queue.popleft()
            result.append(window_start)
            for offset in range(stamp_len):
                if not visited[window_start + offset]:
                    visited[window_start + offset] = True
                    for neighbor in adjacency[window_start + offset]:
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                            queue.append(neighbor)
        return result[::-1] if all(visited) else []
