class Solution:
    def pathSum(self, nums: list[int]) -> int:
        """DFS on encoded tree nodes using depth-position keys for path sums.

        Intuition:
        Each number encodes depth, position, and value. Build a map from
        (depth, position) to value and use DFS to sum all root-to-leaf paths.

        Approach:
        1. Parse each number: first digit = depth, second = position, third = value.
        2. Store in a map keyed by (depth * 10 + position).
        3. DFS from root (1,1), accumulating path sum.
        4. At leaf nodes (no children in map), add path sum to result.

        Complexity:
        Time: O(n)
        Space: O(n)
        """

        def dfs(node: int, path_total: int) -> None:
            if node not in node_map:
                return
            path_total += node_map[node]
            depth, position = divmod(node, 10)
            left_child = (depth + 1) * 10 + (position * 2) - 1
            right_child = left_child + 1
            nonlocal result
            if left_child not in node_map and right_child not in node_map:
                result += path_total
                return
            dfs(left_child, path_total)
            dfs(right_child, path_total)

        result = 0
        node_map = {num // 10: num % 10 for num in nums}
        dfs(11, 0)
        return result
