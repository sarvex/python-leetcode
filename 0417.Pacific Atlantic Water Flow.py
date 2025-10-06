class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """Stack-based DFS to find cells reachable from both oceans.

        Intuition:
        Instead of checking if water flows from each cell to oceans, reverse the
        problem: find all cells reachable from each ocean by flowing upward.
        The intersection gives cells that can reach both oceans.

        Approach:
        - Use stack-based DFS starting from ocean borders
        - Track visited cells for Pacific (top/left edges) and Atlantic (bottom/right edges)
        - For each ocean, traverse upward (to cells with >= height)
        - Return cells present in both visited sets

        Complexity:
        Time: O(m * n) - each cell visited at most twice
        Space: O(m * n) - for visited sets and stack
        """
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def traverse(stack: list[list[int]]) -> set[tuple[int, int]]:
            visited = set()
            while stack:
                i, j = stack.pop()
                visited.add((i, j))
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < rows
                        and 0 <= nj < cols
                        and heights[i][j] <= heights[ni][nj]
                        and (ni, nj) not in visited
                    ):
                        stack.append([ni, nj])
            return visited

        pacific_stack = []
        atlantic_stack = []

        for j in range(cols):
            pacific_stack.append([0, j])
            atlantic_stack.append([rows - 1, j])

        for i in range(rows):
            pacific_stack.append([i, 0])
            atlantic_stack.append([i, cols - 1])

        pacific_reachable = traverse(pacific_stack)
        atlantic_reachable = traverse(atlantic_stack)

        return [
            [i, j]
            for i in range(rows)
            for j in range(cols)
            if (i, j) in pacific_reachable and (i, j) in atlantic_reachable
        ]
