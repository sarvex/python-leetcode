from collections import defaultdict


class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        """Find all processes to kill using DFS from the target process.

        Intuition:
            Build a parent-to-children mapping, then traverse from the kill
            target to collect all descendant processes.

        Approach:
            1. Build an adjacency list mapping parent process to child processes.
            2. DFS from the kill target, collecting all reachable processes.
            3. Return the collected process IDs.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(process: int) -> None:
            result.append(process)
            for child in children_map[process]:
                dfs(child)

        children_map = defaultdict(list)
        for process_id, parent_id in zip(pid, ppid):
            children_map[parent_id].append(process_id)
        result: list[int] = []
        dfs(kill)
        return result
