from collections import defaultdict


class Solution:
    def numOfMinutes(
        self, n: int, head_id: int, manager: list[int], inform_time: list[int]
    ) -> int:
        """Calculate time needed for information to reach all employees.

        Intuition:
            The corporate hierarchy is a tree rooted at the head. The total
            time is the longest path from root to any leaf weighted by inform
            times.

        Approach:
            Build an adjacency list from manager relationships. DFS from the
            head, at each node taking the maximum of recursive times from
            children plus the current node's inform time.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(employee: int) -> int:
            max_time = 0
            for subordinate in subordinates[employee]:
                max_time = max(max_time, dfs(subordinate) + inform_time[employee])
            return max_time

        subordinates: dict[int, list[int]] = defaultdict(list)
        for i, mgr in enumerate(manager):
            subordinates[mgr].append(i)

        return dfs(head_id)
