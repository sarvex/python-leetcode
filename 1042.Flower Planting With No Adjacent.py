from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        """Flower Planting With No Adjacent using greedy graph coloring.

        Intuition:
            Since each garden has at most 3 neighbors and we have 4 flower
            types, a greedy assignment always finds a valid color.

        Approach:
            Build an adjacency list. For each garden, collect the colors used
            by its neighbors, then assign the smallest available color from
            1 to 4.

        Complexity:
            Time: O(n + p) where p is number of paths
            Space: O(n + p)
        """
        adjacency: dict[int, list[int]] = defaultdict(list)
        for garden_a, garden_b in paths:
            a_idx, b_idx = garden_a - 1, garden_b - 1
            adjacency[a_idx].append(b_idx)
            adjacency[b_idx].append(a_idx)
        result = [0] * n
        for garden in range(n):
            used_colors = {result[neighbor] for neighbor in adjacency[garden]}
            for color in range(1, 5):
                if color not in used_colors:
                    result[garden] = color
                    break
        return result
