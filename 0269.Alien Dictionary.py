from collections import deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """Topological sort using BFS to determine alien character ordering.

        Intuition:
            Comparing adjacent words reveals ordering constraints between characters.
            These constraints form a directed graph, and topological sort produces
            a valid ordering if no cycle exists.

        Approach:
            1. Build a directed graph from character ordering constraints found
               by comparing adjacent words.
            2. Track all unique characters that appear in the words.
            3. Compute in-degrees for each character in the graph.
            4. Use BFS (Kahn's algorithm) to produce a topological ordering.
            5. If the ordering includes all unique characters, return it;
               otherwise return empty string (cycle detected).

        Complexity:
            Time: O(C) where C is the total length of all words
            Space: O(1) since the alphabet size is fixed at 26
        """
        graph = [[False] * 26 for _ in range(26)]
        seen = [False] * 26
        unique_count = 0
        num_words = len(words)

        for i in range(num_words - 1):
            for char in words[i]:
                if unique_count == 26:
                    break
                ordinal = ord(char) - ord("a")
                if not seen[ordinal]:
                    unique_count += 1
                    seen[ordinal] = True
            word_len = len(words[i])
            for j in range(word_len):
                if j >= len(words[i + 1]):
                    return ""
                char_a, char_b = words[i][j], words[i + 1][j]
                if char_a == char_b:
                    continue
                ord_a, ord_b = ord(char_a) - ord("a"), ord(char_b) - ord("a")
                if graph[ord_b][ord_a]:
                    return ""
                graph[ord_a][ord_b] = True
                break

        for char in words[num_words - 1]:
            if unique_count == 26:
                break
            ordinal = ord(char) - ord("a")
            if not seen[ordinal]:
                unique_count += 1
                seen[ordinal] = True

        in_degree = [0] * 26
        for i in range(26):
            for j in range(26):
                if i != j and seen[i] and seen[j] and graph[i][j]:
                    in_degree[j] += 1

        queue = deque()
        ordering: list[str] = []
        for i in range(26):
            if seen[i] and in_degree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ordering.append(chr(current + ord("a")))
            for i in range(26):
                if seen[i] and i != current and graph[current][i]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)

        return "" if len(ordering) < unique_count else "".join(ordering)
