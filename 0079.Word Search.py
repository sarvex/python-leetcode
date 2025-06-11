from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Backtracking with DFS to find word in 2D board.

        Intuition:
        Use depth-first search with backtracking to explore all possible paths
        in the board that could form the target word. Mark visited cells to avoid
        revisiting them during the same path exploration.

        Approach:
        1. For each cell in the board, try to start the word search from there
        2. Use DFS to explore adjacent cells (up, right, down, left)
        3. Mark visited cells temporarily during exploration
        4. Backtrack when a path doesn't lead to a solution

        Complexity:
        Time: O(m*n*4^L) where m,n are board dimensions and L is word length
        Space: O(L) for recursion stack depth
        """
        def dfs(i: int, j: int, k: int) -> bool:
            # Base cases
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            # Mark as visited
            original = board[i][j]
            board[i][j] = '#'

            # Explore in all four directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for di, dj in directions:
                if dfs(i + di, j + dj, k + 1):
                    return True

            # Backtrack
            board[i][j] = original
            return False

        if not board or not board[0] or not word:
            return False

        m, n = len(board), len(board[0])
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
