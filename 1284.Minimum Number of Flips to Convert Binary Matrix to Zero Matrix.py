from collections import deque


class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        """Minimum flips to convert binary matrix to zero matrix.

        Intuition:
            Each cell flip toggles the cell and its neighbors. Use BFS over bitmask
            states to find the shortest path from the initial state to the all-zero state.

        Approach:
            Encode the matrix as a bitmask. BFS from the initial state, generating all
            possible next states by flipping each cell and its neighbors. Return the
            number of steps when the zero state is reached.

        Complexity:
            Time: O(2^(m*n) * m * n)
            Space: O(2^(m*n))
        """
        rows, cols = len(mat), len(mat[0])
        initial_state = sum(
            1 << (i * cols + j) for i in range(rows) for j in range(cols) if mat[i][j]
        )
        queue = deque([initial_state])
        visited: set[int] = {initial_state}
        steps = 0
        directions = [0, -1, 0, 1, 0, 0]

        while queue:
            for _ in range(len(queue)):
                state = queue.popleft()
                if state == 0:
                    return steps
                for i in range(rows):
                    for j in range(cols):
                        next_state = state
                        for k in range(5):
                            neighbor_row = i + directions[k]
                            neighbor_col = j + directions[k + 1]
                            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                                bit = 1 << (neighbor_row * cols + neighbor_col)
                                next_state ^= bit
                        if next_state not in visited:
                            visited.add(next_state)
                            queue.append(next_state)
            steps += 1
        return -1
