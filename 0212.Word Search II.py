from itertools import pairwise


class Trie:
    """Trie data structure for efficient prefix-based word lookup."""

    def __init__(self) -> None:
        """Initialize trie node with children array and word reference."""
        self.children: list[Trie | None] = [None] * 26
        self.ref: int = -1

    def insert(self, word: str, ref: int) -> None:
        """Insert a word into the trie with its index reference."""
        node = self
        for char in word:
            index = ord(char) - ord("a")
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.ref = ref


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """Trie-based DFS backtracking search on the board.

        Intuition:
            Build a trie from all words, then DFS from every cell on the board.
            The trie allows pruning paths that cannot lead to any word.

        Approach:
            1. Insert all words into a trie with their index as reference.
            2. For each cell, start a DFS that follows trie children.
            3. When a word reference is found, record it and reset to avoid duplicates.
            4. Mark visited cells with '#' and restore after backtracking.

        Complexity:
            Time: O(m * n * 4^L) where L is max word length
            Space: O(W * L) for the trie where W is number of words
        """

        def dfs(node: Trie, row: int, col: int) -> None:
            index = ord(board[row][col]) - ord("a")
            if node.children[index] is None:
                return
            node = node.children[index]
            if node.ref >= 0:
                result.append(words[node.ref])
                node.ref = -1
            original = board[row][col]
            board[row][col] = "#"
            for delta_row, delta_col in pairwise((-1, 0, 1, 0, -1)):
                next_row, next_col = row + delta_row, col + delta_col
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and board[next_row][next_col] != "#"
                ):
                    dfs(node, next_row, next_col)
            board[row][col] = original

        tree = Trie()
        for idx, word in enumerate(words):
            tree.insert(word, idx)
        rows, cols = len(board), len(board[0])
        result: list[str] = []
        for row in range(rows):
            for col in range(cols):
                dfs(tree, row, col)
        return result
