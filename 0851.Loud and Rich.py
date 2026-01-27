from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        """DFS with memoization on the richer-than graph.

        Intuition:
            Build a graph where edges point from less-rich to richer people. For
            each person, DFS through all people richer than them and track the
            quietest one found.

        Approach:
            1. Build adjacency list from richer relations (b -> a means a is richer than b)
            2. DFS from each person, propagating the quietest ancestor
            3. Memoize results to avoid recomputation

        Complexity:
            Time: O(V + E) where V is number of people and E is number of richer pairs
            Space: O(V + E) for the graph and result array
        """

        def dfs(person: int) -> None:
            if result[person] != -1:
                return
            result[person] = person
            for richer_person in graph[person]:
                dfs(richer_person)
                if quiet[result[richer_person]] < quiet[result[person]]:
                    result[person] = result[richer_person]

        graph: dict[int, list[int]] = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
        num_people = len(quiet)
        result = [-1] * num_people
        for person in range(num_people):
            dfs(person)
        return result
