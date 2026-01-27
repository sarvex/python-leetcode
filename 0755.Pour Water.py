class Solution:
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        """Simulate water drops falling left then right from position k.

        Intuition:
            Each water drop tries to flow left to the lowest reachable point;
            if none exists, it tries flowing right. Otherwise it stays at k.

        Approach:
            1. For each drop, scan left for a lower position, tracking the
               lowest point found.
            2. If no lower point on the left, scan right similarly.
            3. Increment the height at the chosen position.

        Complexity:
            Time: O(V * N) where V = volume, N = len(heights)
            Space: O(1) extra
        """
        for _ in range(volume):
            for direction in (-1, 1):
                current = lowest = k
                while (
                    0 <= current + direction < len(heights)
                    and heights[current + direction] <= heights[current]
                ):
                    if heights[current + direction] < heights[current]:
                        lowest = current + direction
                    current += direction
                if lowest != k:
                    heights[lowest] += 1
                    break
            else:
                heights[k] += 1
        return heights
