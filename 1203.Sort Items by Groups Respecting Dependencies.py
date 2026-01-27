from collections import deque


class Solution:
    def sortItems(
        self, n: int, m: int, group: list[int], before_items: list[list[int]]
    ) -> list[int]:
        """Topological sort of items respecting both group and item dependencies.

        Intuition:
            Items within the same group must be contiguous in the output. We need
            two levels of topological sort: one for groups and one for items
            within each group.

        Approach:
            Assign unique group IDs to ungrouped items. Build intra-group and
            inter-group dependency graphs. Topologically sort groups first, then
            sort items within each group. Concatenate results in group order.

        Complexity:
            Time: O(n + m + E) where E is total dependency edges
            Space: O(n + m + E)
        """

        def topological_sort(
            degree: list[int], graph: list[list[int]], items: range | list[int]
        ) -> list[int]:
            queue = deque(item for item in items if degree[item] == 0)
            result: list[int] = []
            while queue:
                item = queue.popleft()
                result.append(item)
                for dependent in graph[item]:
                    degree[dependent] -= 1
                    if degree[dependent] == 0:
                        queue.append(dependent)
            return result if len(result) == len(items) else []

        next_group_id = m
        group_items: list[list[int]] = [[] for _ in range(n + m)]
        for i, grp in enumerate(group):
            if grp == -1:
                group[i] = next_group_id
                next_group_id += 1
            group_items[group[i]].append(i)

        item_degree = [0] * n
        group_degree = [0] * (n + m)
        item_graph: list[list[int]] = [[] for _ in range(n)]
        group_graph: list[list[int]] = [[] for _ in range(n + m)]
        for i, group_i in enumerate(group):
            for j in before_items[i]:
                group_j = group[j]
                if group_i == group_j:
                    item_degree[i] += 1
                    item_graph[j].append(i)
                else:
                    group_degree[group_i] += 1
                    group_graph[group_j].append(group_i)

        group_order = topological_sort(group_degree, group_graph, range(n + m))
        if not group_order:
            return []
        result: list[int] = []
        for group_id in group_order:
            items = group_items[group_id]
            item_order = topological_sort(item_degree, item_graph, items)
            if len(items) != len(item_order):
                return []
            result.extend(item_order)
        return result
