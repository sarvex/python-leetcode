from itertools import pairwise


class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        """Bitmask DP (TSP variant) to find shortest superstring of all words.

        Intuition:
            This is equivalent to finding a shortest Hamiltonian path in a graph
            where edge weights represent overlap lengths between words. We maximize
            total overlap to minimize the superstring length.

        Approach:
            1. Build overlap graph: g[i][j] = max suffix-prefix overlap from word i to j.
            2. Use bitmask DP: dp[mask][j] = max total overlap ending at word j using words in mask.
            3. Track parent pointers to reconstruct the optimal word ordering.
            4. Build the superstring by appending non-overlapping suffixes.

        Complexity:
            Time: O(2^n * n^2 + n^2 * m) — bitmask DP plus overlap computation
            Space: O(2^n * n) — DP and parent tables
        """
        num_words = len(words)
        overlap = [[0] * num_words for _ in range(num_words)]
        for i, word_a in enumerate(words):
            for j, word_b in enumerate(words):
                if i != j:
                    for length in range(min(len(word_a), len(word_b)), 0, -1):
                        if word_a[-length:] == word_b[:length]:
                            overlap[i][j] = length
                            break
        dp = [[0] * num_words for _ in range(1 << num_words)]
        parent = [[-1] * num_words for _ in range(1 << num_words)]
        for mask in range(1 << num_words):
            for current in range(num_words):
                if (mask >> current) & 1:
                    prev_mask = mask ^ (1 << current)
                    for prev in range(num_words):
                        if (prev_mask >> prev) & 1:
                            value = dp[prev_mask][prev] + overlap[prev][current]
                            if value > dp[mask][current]:
                                dp[mask][current] = value
                                parent[mask][current] = prev
        last_word = 0
        for idx in range(num_words):
            if dp[-1][idx] > dp[-1][last_word]:
                last_word = idx
        path = [last_word]
        mask = (1 << num_words) - 1
        while parent[mask][last_word] != -1:
            mask, last_word = mask ^ (1 << last_word), parent[mask][last_word]
            path.append(last_word)
        path = path[::-1]
        visited = set(path)
        path.extend([idx for idx in range(num_words) if idx not in visited])
        parts = [words[path[0]]] + [
            words[j][overlap[i][j] :] for i, j in pairwise(path)
        ]
        return "".join(parts)
