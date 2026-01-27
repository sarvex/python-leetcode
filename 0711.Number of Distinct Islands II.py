class Solution:
    def numDistinctIslands2(self, grid: list[list[int]]) -> int:
        """Count distinct islands considering rotations and reflections.

        Intuition:
            Two islands are the same if one can be transformed into the other
            via rotation or reflection. Generate all 8 transformations and
            normalize each to find canonical forms.

        Approach:
            1. DFS to find each island's cell coordinates.
            2. For each island, generate all 8 rotation/reflection variants.
            3. Normalize each variant by sorting and translating to origin.
            4. Use the lexicographically smallest variant as the canonical form.
            5. Store canonical forms in a set and return its size.

        Complexity:
            Time: O(m * n * log(m * n)) for sorting island shapes
            Space: O(m * n) for visited cells and shape storage
        """

        def dfs(row: int, col: int, shape: list[list[int]]) -> None:
            shape.append([row, col])
            grid[row][col] = 0
            for delta_row, delta_col in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                next_row, next_col = row + delta_row, col + delta_col
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] == 1
                ):
                    dfs(next_row, next_col, shape)

        def normalize(shape: list[list[int]]) -> tuple[tuple[int, int], ...]:
            transformations: list[list[list[int]]] = [[] for _ in range(8)]
            for row, col in shape:
                transformations[0].append([row, col])
                transformations[1].append([row, -col])
                transformations[2].append([-row, col])
                transformations[3].append([-row, -col])
                transformations[4].append([col, row])
                transformations[5].append([col, -row])
                transformations[6].append([-col, row])
                transformations[7].append([-col, -row])
            for variant in transformations:
                variant.sort()
                for idx in range(len(variant) - 1, -1, -1):
                    variant[idx][0] -= variant[0][0]
                    variant[idx][1] -= variant[0][1]
            transformations.sort()
            return tuple(tuple(cell) for cell in transformations[0])

        rows, cols = len(grid), len(grid[0])
        seen: set[tuple[tuple[int, int], ...]] = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    shape: list[list[int]] = []
                    dfs(row, col, shape)
                    seen.add(normalize(shape))
        return len(seen)
