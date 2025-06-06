from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """BFS approach to simulate rotting process

        Intuition:
        Use BFS to simulate the rotting process, where each minute all adjacent fresh
        oranges to a rotten one become rotten simultaneously.

        Approach:
        1. Count fresh oranges and collect positions of rotten oranges in a queue
        2. Perform BFS from all rotten oranges, incrementing minutes for each level
        3. Track remaining fresh oranges and return minutes when all are rotten
        4. Return -1 if any fresh oranges remain unreachable

        Complexity:
        Time: O(m*n) where m and n are the dimensions of the grid
        Space: O(m*n) for the queue in worst case
        """
        m, n = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()

        # Initial scan to count fresh oranges and collect rotten ones
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    rotten.append((i, j))

        # No fresh oranges means we're already done
        if fresh == 0:
            return 0

        # Directions: up, right, down, left
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        minutes = 0

        # BFS traversal
        while rotten and fresh > 0:
            minutes += 1

            # Process all currently rotten oranges
            for _ in range(len(rotten)):
                i, j = rotten.popleft()

                # Check all four adjacent cells
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    # If adjacent cell is valid and has a fresh orange
                    if (0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1):
                        grid[ni][nj] = 2  # Make it rotten
                        fresh -= 1
                        rotten.append((ni, nj))

        # If any fresh oranges remain, they can't be reached
        return minutes if fresh == 0 else -1
